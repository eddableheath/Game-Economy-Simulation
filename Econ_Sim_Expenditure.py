##----------------------------------------------------------------------------##
##                            Economy Simulation                              ##
##----------------------------------------------------------------------------##

from numpy import random

## Expenditure -----------------------------------------------------------------

# Spendable item class
class spend_item(object):
    '''Generic speable item which will give generated amount spent each day'''

    item_type = 'Expenditure'

    def __init__(self, name, cost, probability, daily_max_usage): #The attributes from the initilisation
        self.name = name
        self.cost = cost
        self.prob = probability
        self.usage = daily_max_usage

    def probable_use(self):
        if self.usage != 0:
            prob_use = 0
            for i in range(self.usage):
                repeat_use_prob = self.prob ** (i+1)
                prob_use += random.choice([0, 1], 1, p = [1 - repeat_use_prob, repeat_use_prob])
        else:
            prob_use = 42
        return prob_use

    def probable_spend(self):
        return self.probable_use() * self.cost
