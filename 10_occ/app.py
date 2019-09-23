#David Xiedeng
#SoftDev1 pd 1
#K 10 -- Jinja Tuning
#2019-09-23

from flask import Flask, render_template; 
import random
app = Flask(__name__)

occupations = {}

#read from data/occupations and make dict
def readOccupations():
  file = open("data/occupations.csv", "r")
  ## outputs to lines a list, with each line as a string item in lines
  lines = file.readlines()[1:]

  for i in range(len(lines)):
  ## lines does not contain ", split by comma
      if lines[i].find('\"') == -1:
          lines[i] = lines[i].split(',')
      else:
  ## lines contain " and must get rid of leading ", split by ",
          lines[i] = lines[i].strip('\"').split('\",')
  ## outputted dictionary

  for line in lines:
    occupations.update({line[0]: float(line[1].strip())})
    
#readOccupations()
#print(occupations)

## input: dictionary d {string, float}
## output: random occupation (string)
def random_occupation(d):
  rNum = random.uniform(0, d["Total"])
  low = 0
  #loop through dict, d
  for key in out:
    #skip ["Total"]
    #range [lower_range, upper _range]
    if rNum >= low and rNum <= d[key] + low:
      return "" + key
    low = low + d[key]

