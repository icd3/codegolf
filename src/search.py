import sys
import json
import re
r={}
t=sys.stdout
def w(p):t.write(p);t.flush()
def x(f):
 for l in f:
  l=l.strip().partition(':')
  if l[2]:r[c(l[2])]=l[0].strip()
def c(t):return re.sub(r'([\?!-])',' \1',re.sub(r'([/\(\):\.,;])','',t)).lower()
x(open(sys.argv[1],'r'))
while 1:
 w('> ')
 try:i=sys.stdin.readline()
 except:break
 if i:
  i=c(i).split()
  s=[]
  for k in r.keys():
   for u in i:
    if not u in k:break
   else:s.append(r[k])
  w(json.dumps(s))
