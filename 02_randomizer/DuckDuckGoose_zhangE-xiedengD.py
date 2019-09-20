#David Xiedeng
#SoftDev1 pd 1
#K 02 -- NO-body expects the Spanish Inquisition!
#2019-09-11 

import random

Krewes = {
    'orpheus':['Emily', 'Kevin', 'Vishwaa'],
    'rex':['Will', 'Joe', 'Jack']
}

##print (Krewes.keys())
key = list(Krewes.keys())[random.randint(0, len(Krewes) - 1)]
spot = Krewes[key]
print (spot[random.randint(0, len(spot) - 1)])
