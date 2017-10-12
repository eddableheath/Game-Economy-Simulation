##----------------------------------------------------------------------------##
##                            Economy Simulation                              ##
##----------------------------------------------------------------------------##

# functions

def n_days_money(n, items):
    '''gives n days worth of spending given probabilities and cost'''
    spending = {'daily' : {}, 'total' : 0}
    for i in range(1, n+1):
        daily_money = 0
        for entry in items:
            daily_money += entry.probable_spend()
        spending['daily'][i] = daily_money
    spending['total'] = sum(spending['daily'].values())
    return spending
