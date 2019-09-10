import random
Krewes = {
    'orpheus':['Emily', 'Kevin', 'Vishwaa'],
    'rex':['Will', 'Joe', ' Jack']
}

print (Krewes.keys())
key = Krewes.keys()[random.randint(0,1)]
print Krewes[key]
