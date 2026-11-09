# Usage (from latex/tark2027/): python3 scripts/check_lost_sentences.py <rev> [file] [files to search...]
# Lists sentences in <rev>:file that no longer occur in the current files (comments and \modified{ ignored).
# Run after every cut; every hit must be a CUTS.md row.
import re,subprocess,sys
rev=sys.argv[1]; f=sys.argv[2] if len(sys.argv)>2 else 'body.tex'
old=subprocess.run(['git','show',f'{rev}:latex/tark2027/{f}'],capture_output=True,text=True).stdout
new=''.join(open(x).read() for x in sys.argv[3:]) if len(sys.argv)>3 else open(f).read()
def sents(t):
    t=re.sub(r'(?<!\\)%.*','',t)
    t=re.sub(r'\\modified\{','',t)
    t=re.sub(r'\s+',' ',t)
    return [x.strip() for x in re.split(r'(?<=[.?!])\s+(?=[A-Z\\])',t) if len(x.strip())>25]
N=re.sub(r'\s+',' ',re.sub(r'\\modified\{','',re.sub(r'(?<!\\)%.*','',new)))
for s in sents(old):
    key=s[:60]
    if key not in N: print('-',s[:220]); print()
