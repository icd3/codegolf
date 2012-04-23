import sys,json,re
r={}
t=sys.stdout
def w(p):t.write(p);t.flush()
def x(f):
 for l in f:
  l=l.strip().partition(' : ');s=l[0];t=c(l[2])
  if t in r:r[t].append(s)
  else:r[t]=[s]
def c(t):return re.sub(r'([-])',' \1 ',re.sub(r'([?!])',' \1',re.sub(r'([/():.,;])','',t.lower())))
x(open(sys.argv[1],'r'))
while 1:
 w('> ')
 i=sys.stdin.readline()
 if i:
  i=c(i).split()
  s=[]
  for k in r.keys():
   for u in i:
    if not u in k:break
   else:s.extend(r[k])
  w(json.dumps(s))
