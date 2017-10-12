##----------------------------------------------------------------------------##
##                            Economy Simulation                              ##
##----------------------------------------------------------------------------##

from numpy import random, ceil

## Expenditure -----------------------------------------------------------------

# Spendable item class
class spend_item(object):
    '''Generic speable item which will give generated amount spent each day'''

    item_type = 'Expenditure'

    def __init__(self, name, cost, mean_use, probability, daily_max_usage): #The attributes from the initilisation
        self.name = name
        self.cost = cost
        self.prob = probability
        self.usage = mean_use
        self.max_use = daily_max_usage

    def probable_use(self):
        used = random.choice([0,1], 1, p = [1 - self.prob, self.prob])
        if used == 0:
            return 0
        if used == 1:
            return self.usage

    def probable_spend(self):
        return self.probable_use() * self.cost

# items

snatching = spend_item('snatching', 25, 6, 0.7, 0)
battery = spend_item('battery', 65, 1.2, 0.014, 2)
black_hole = spend_item('black_hole', 1500, 1, 0.025, 1)
cloak = spend_item('Invisibility_cloak', 125, 1.6, 0.1, 3)
radar = spend_item('radar', 200, 1.5, 0.19, 3)
smoke_screen = spend_item('smoke_screen', 55, 3.5, 0.22, 0)
vest = spend_item('snatch_proof_vest', 40, 2.5, 0.047, 0)
strongbox = spend_item('strong box', 775, 1, 0.015, 1)
tent = spend_item('tent', 75, 1.01, 0.086, 1)

expenditure_items = [snatching,
                    battery,
                    black_hole,
                    cloak,
                    radar,
                    smoke_screen,
                    vest,
                    strongbox,
                    tent]
