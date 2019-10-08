#David Xiedeng
#SoftDev1 pd 1
#K 06 -- StI/O: Divine your Destiny!
#2019-09-17 

import random

## Goal: Write a Python script to read in the file and build an appropriate dictionary from it.
##      Make sure the percentages are stored as numbers.

file = open('occupations.csv', 'r')
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
out = dict()

for line in lines:
        out.update({line[0]: float(line[1].strip())})
#print (out)
#print()

## Goal: Create a function that randomly returns an occupations
##      based on the value it is weighted by



## input: dictionary d {string, float}
## output: random occupation (string)
def random_occupation(d):
    ## dictionary with upper ranges, uses same keys
    ranges = dict()
    keys = list(d)
    sum = 0
    for i in range(len(d)):
        sum += d.get(keys[i])
        ranges.update({keys[i] : sum})

    values = list(ranges.values())

    ## randomizing within the highest occupation limit
    value = random.uniform(0, values[len(values) - 2])
    prev = 0
    for val in values:
        if value <= val and value >= prev:
            return keys[values.index(val)]
        prev = val

#print(random_occupation(out))

## input: dictionary d {string, float}
## output: random occupation (string)
def random_occupation_2(d):
  rNum = random.uniform(0, d["Total"])
  low = 0
  #loop through dict, d
  for key in out:
    #skip ["Total"]
    #range [lower_range, upper _range]
      if rNum >= low and rNum <= d[key] + low:
        return "" + key
      low = low + d[key]

##print(random_occupation_2(out))

## checks percentages of getting an occupation over many tries
def check_percentage(keys):
    total = 0
    ## dictionary of occupation(string) : hits by randomizer(int)
    d = {i : 0 for i in keys}
    for i in range(1, 2 ** 19):
        total += 1
        for key in keys:
            if (random_occupation_2(out) == key):
                d.update({key : d.get(key) + 1})
    ## format and print "occupation: percent %"
    for j in keys:
        print(j + ':', int(d.get(j) / total * 1000) / 10, '%')

check_percentage(list(out)[:-1])
