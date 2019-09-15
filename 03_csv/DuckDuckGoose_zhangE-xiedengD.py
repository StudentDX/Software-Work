import random

file = open('occupations.csv','r')
lines = file.readlines()[1:]

for i in range(len(lines)):
    if lines[i].find('\"') == -1:
        lines[i] = lines[i].split(',')
    else:
        lines[i] = lines[i].strip('\"').split('\",')

out = dict()

### parallel, reversed dict that has ranges between each key
copy = dict()
sum = 0

for line in lines:
    out.update({line[0] : float(line[1].strip())})
    sum = sum + float(line[1].strip())
    copy.update({sum : line[0]})
print(out)

## Goal: Create a function that randomly returns an occupations
## based on the value it is weighted by

#for el in copy:
# print ("{},{}".format(el, copy[el]))

print()
#print(copy)
#print (list(copy.keys())[len(copy) - 2])
### choosing a value from parallel dict copy
value = random.uniform(0, list(copy.keys())[len(copy) - 2])

#print(value)
for val in copy:
  if value < val:
    print (copy[val])
    break