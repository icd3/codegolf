import sys
import json
import re
r={}
t=sys.stdout
def p(s,c,d): return s.replace(c,d)
def x(f):
 for l in f:
  l=l.strip().partition(':')
  if l[2]:r[c(l[2])]=l[0].strip()
def c(t):return p(p(p(p(p(p(p(p(p(p(t.lower(),'/',''),'(',''),')',''),':',''),'.',''),',',''),';',''),'?',' ?'),'!',' !'),'-',' - ')
x(open(sys.argv[1],'r'))
t.flush()
while 1:
 t.write('> '); t.flush()
 try:i=sys.stdin.readline()
 except:break;
 if i:
  i=c(i).split()
  s=[]
  for k in r.keys():
   for u in i:
    if not u in k:break
   else:s.append(r[k])
  t.write(json.dumps(s))
  t.flush()
