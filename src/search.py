import sys
import json
import codecs

reviews = {}

def index(file):
  f = codecs.open(file, 'r', 'utf-8')
  for line in f:
    line = line.strip()
    if line:
      line = line.partition(':')
      reviews[clean(line[2])] = line[0].strip()
  f.close()

def query(input):
  results = []
  for key in reviews.keys():
    for term in input:
      if not term in key: break
    else:
      results.append(reviews[key])
  return results

def clean(text):
  return (
    text
    .lower()
    .replace('/', '')
    .replace('(', '')
    .replace(')', '')
    .replace(':', '')
    .replace('.', '')
    .replace(',', '')
    .replace(';', '')
    .replace(';', '')
    .replace('?', ' ?')
    .replace('!', ' !')
    .replace('-', ' - '))


index( sys.argv[1])
sys.stdout.flush()
while True:
  sys.stdout.write('> '); sys.stdout.flush()
  try: inpt = sys.stdin.readline()
  except: break;
  if not inpt: continue
  inpt = clean(inpt)
  inpt = inpt.split()
  sys.stdout.write( json.dumps( query(inpt)))
  sys.stdout.flush()
  
sys.stdout.flush()
