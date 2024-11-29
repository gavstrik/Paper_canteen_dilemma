library(ggplot2)
library(ggeffects)
library(sjmisc)
library(lme4)

cd <- read.csv("../../Data/data.csv")

# explanation of the data:
# "code" is the identifier for each subject
# "exp" is the identifier for each experiment done either at Amazon Mechanical Turk (AMT), 
# DTU class on AI and Multi-agent systems (DTU1), or DTU introductory class on AI (DTU2).
# "session" is the experimental session (only one for DTU1 and DTU2, but several for AMT)
# "group" is the pair number of two subjects playing with each other in each session
# "round" is the round number. There are 10 rounds in the AMT experiments, but 30 rounds in DTU1 and DTU2
# "arrival" is the players arrival time
# "certainty" is the reported likelihood by subjects that they will coordinate
# "bonus" is the penalty (in dollars) for this round
# "cutoff" is the arrival time reported by subjects they think is enough for safe coordination
# "fault" is a whether the players think that miscoordination was their partners fault
# "simple" is the answer to whether the players there is common knowledge or not.
# "payoff" is what the subjects got payed
# "strategy" is a free text survey about what strategy the players used.

tail(cd)

# make a new column giving each pair of subjects in each session an unique id:
cd$pair_id <- paste(cd$session, cd$group)

# change arrival times to consecutive integers
cd$arr <- as.integer(as.factor(cd$arrival))

# keep only the needed columns and make a new dataframe
keeps <- c("exp", "pair_id", "code", "round", "arr", "choice", "certainty")
Data <- cd[keeps]
head(Data)

# convert categorical data into factors
Data <- within(Data, {
  choice <- factor(choice, levels = 0:1, labels = c("office", "canteen"))
  exp <- factor(exp)
})

str(Data)

# check that all variables are represented by subjects
xtabs(~ choice + arr, data=Data)
xtabs(~ choice + certainty, data=Data)
xtabs(~ choice + round, data=Data)
xtabs(~ choice + exp, data=Data)

head(Data)

# use the glmer() function for a generalized mixed model. We start
# with the most general mixed model incorporating all fixed and
# random effects in a logarithmic regression that we can expect
# to play a role. The first fixed effect is the arrival time which
# we already know determines most of the probability of choosing
# either the canteen or the office. Next, the we can expect the 
# round number to play a role: maybe people learn during play.
# Third, the kinds of players and settings may play a role, which
# is captured by the exp-factor, which denotes whether the players 
# are from Amazon Mechanical Turk of from DTU1 or DTU2. We also want 
# to check for interactions between exp and arrival time as there may
# be a difference between when MTurk players and DTU players start to
# choose the office.

#m0 <- glmer(choice ~ arr + exp + round + exp:arr +
#              (1 | pair_id) + (1 | code), 
#            data = Data, family = binomial, 
#            glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000)))
#summary(m0)
# the summary shows that round is not significant, so we can remove it from the
# model. Also the random effect from the individual players ('code') is quite 
# small, compared to the random effect from the pairs ('pair_id'). We therefore
# try to remove the random effect from 'code'. Note that arr+exp+exp:arr=arr*exp

m1 <- glmer(choice ~ arr*exp + (1 | pair_id), 
            data = Data, family = binomial,
            glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000)))

summary(m1)
# this summary shows significant effects from all variables. We also see that
# both DTU-experiments differ from the AMT-experiment. Let's make a plot:
library(sjPlot) 
plot_model(m1, type = "int")

# However, we cannot see, also not in the plot,
# whether the two DTU-experiments differ from each other. To test for that, we
# relevel the experiments so that DTU1 is compared with the two other exp.

Data$exp = relevel(Data$exp, ref= "DTU1")
m2 <- glmer(choice ~ arr*exp + (1 | pair_id), 
            data = Data, family = binomial,
            glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000)))

summary(m2)
# the summary shows that DTU2 is not significant different from DTU. Thus, we 
# can try to combine them and check if this is ok with an anova test.

Data$DTU = 1*(Data$exp != "AMT") # DTU becomes 1 and AMT becomes 0
head(Data)
m3 <- glmer(choice ~ arr*DTU + (1 | pair_id), data = Data, family = binomial) # should I use binomial(link = "logit") instead?
summary(m3)
anova(m2, m3)
# oops. anova says that the two models are weakly but 
# significantly different. But since the regression fits both the intercept
# and the slope, maybe we can check if the two DTU experiments have a common
# slope but not a common intercept:

m4 <- glmer(choice ~ arr:DTU + arr + exp + (1 | pair_id), data = Data, family = binomial) # : means only interaction
summary(m4)
anova(m2, m4)
# yes, the slope can be reduced to only two. Now we have three intercepts
# and two slopes. We also can try to reduce the intercepts instead:

m5 <- glmer(choice ~ arr:exp + arr + DTU + (1 | pair_id), data = Data, family = binomial) # : means only interaction
summary(m5)
anova(m2, m5)
# yes again. This means that we could reduce the model to two intercepts 
# and three slopes or to three intercepts and two slopes. Ergo we only can
# partially combine the DTU1 and DTU2 experiments.


plot_model(m1, type = "int")
ggpredict(m1, c("exp", "arr")) %>% plot()
myplot <- ggpredict(m1, c("arr", "exp")) %>% plot()

plot(myplot) + 
  labs(
    x = "arrival time", 
    y = "canteen", 
    colour = "experiment",
    title = "",
  ) +
  scale_x_continuous(labels = c("8:00", "8:10", "8:20", "8:30", "8:40", "8:50", "9:00", "9:10"), breaks = c(1:8)) +
  scale_colour_brewer(palette = "Set1", labels = c("MTurk", "DTU1", "DTU2")) +
  theme(panel.grid.minor = element_blank())


# lets have a look at the fitted probabilities:
predict(m2)
Data$pred = plogis(predict(m2)) # det er sandsynlighederne for at gĺ i kantinen for hver spiller
tail(Data)