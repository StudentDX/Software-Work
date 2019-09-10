import random
Krewes = {
    'orpheus':['Emily', 'Kevin', 'Vishwaa'],
    'rex':['Will', 'Joe', 'Jack']
}

print (Krewes.keys())
key = Krewes.keys()[random.randint(0, len(Krewes) - 1)]
spot = Krewes[key]
print spot[random.randint(0, len(spot) - 1)]
