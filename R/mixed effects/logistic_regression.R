setwd("C:/Users/hjl161/Documents/Papers/Paper_canteen_dilemma/R/mixed effects")

# install.packages(c("ggplot2", "GGally", "reshape2", "lme4", "compiler", "parallel", "boot", "lattice"))
# install.packages("cowplot")

require(ggplot2)
require(GGally)
require(reshape2)
require(lme4)
require(compiler)
require(parallel)
require(boot)
require(lattice)
require(cowplot)

cd <- read.csv("../../Data/data.csv")

# explanation of the data:
# "code" is the identifier for each subject
# "exp" is the identifier for each experiment done either at AMT, DTU1 or DTU2
# "session" is the experimental session (only one for DTU1 and DTU2, but several for AMT)
# "group" is the pair of subjects playing with each other in each session
# "round" is the round number. There are 10 rounds in the AMT experiments, but 30 rounds in DTU1 and DTU2
# "arrival" is the arrival time
# "certainty" is the reported likelihood by subjects that they will coordinate
# "bonus" is the penalty (in dollars) for this round
# "cutoff" is the arrival time reported by subjects they think is enough for safe coordination
# "payoff" is what the subjects got payed

head(cd)

# make a new column giving each pair of subjects an unique id:
cd$pair_id <- paste(cd$session, cd$group)
head(cd)

# change arrival times to consecutive numbers
cd$arr <- as.numeric(as.factor(cd$arrival))
tail(cd)

keeps <- c("exp", "pair_id", "code", "round", "arr", "choice", "certainty")
Data <- cd[keeps]
head(Data)

# convert columns into factors
Data <- within(Data, {
  choice <- factor(choice, levels = 0:1, labels = c("office", "canteen"))
  arr <- factor(arr)
  exp <- factor(exp)
  certainty <- factor(certainty)
  round <- factor(round)
})

str(Data)

# check that all variables are represented by subjects
xtabs(~ choice + arrival, data=cd)
xtabs(~ choice + certainty, data=cd)
xtabs(~ choice + round, data=cd)
xtabs(~ choice + cutoff, data=cd)
xtabs(~ choice + experiment, data=cd)


# a very simple logistic regression
#logistic <- glm(choice ~ arr, data=Data, family="binomial")
#summary(logistic)

log2 <- glm(choice ~ arr*exp, data=Data, family="binomial")
summary(log2)


## Now calculate the overall "Pseudo R-squared" and its p-value

## NOTE: Since we are doing logistic regression...
## Null devaince = 2*(0 - LogLikelihood(null model))
##               = -2*LogLikihood(null model)
## Residual deviacne = 2*(0 - LogLikelihood(proposed model))
##                   = -2*LogLikelihood(proposed model)
ll.null <- log2$null.deviance/-2
ll.proposed <- log2$deviance/-2

## McFadden's Pseudo R^2 = [ LL(Null) - LL(Proposed) ] / LL(Null)
(ll.null - ll.proposed) / ll.null

## chi-square value = 2*(LL(Proposed) - LL(Null))
## p-value = 1 - pchisq(chi-square value, df = 2-1)
1 - pchisq(2*(ll.proposed - ll.null), df=1)
1 - pchisq((log2$null.deviance - log2$deviance), df=1)

## The p-value for the R^2
1 - pchisq(2*(ll.proposed - ll.null), df=(length(log2$coefficients)-1))

predicted.data <- data.frame(probability.of.choosing.canteen=log2$fitted.values, arr=Data$arr, choice=Data$choice, exp=Data$exp)
predicted.data <- predicted.data[order(predicted.data$probability.of.choosing.canteen, decreasing=FALSE),]
#predicted.data$rank <- c(1,2,3,4,5,6,7,8)

ggplot(data=predicted.data, aes(x=arr, y=probability.of.choosing.canteen, colour = exp)) + 
  geom_point() +
  #geom_smooth(method = "glm", method.args = list(family = "binomial"), se = FALSE) +
  xlab("Arrival") + 
  ylab("Predicted probability of choosing canteen")



m <- glmer(choice ~ exp*arr + (1 | code), data = Data, family = binomial, 
           control = glmerControl(optimizer = "bobyqa"), nAGQ = 10)
summary(m)




