##----------------------------------------------------------------------------##
##                            Economy Simulation                              ##
##----------------------------------------------------------------------------##

## Main File -------------------------------------------------------------------

# Imports
import numpy as np
import scipy as sp
import Econ_Sim_Expenditure as exp
import Econ_Sim_Income as inc
import Econ_Sim_Functionality as func

# Spend items
exp_items = exp.expenditure_items

days_spend_7 = func.n_days_spend(7, exp_items)
days_spend_14 = func.n_days_spend(14, exp_items)

#for i in days_spend_7:
#    print i, days_spend_7[i]

#for j in days_spend_14:
#    print j, days_spend_14[j]

#print func.IAP_income(inc.IAP_items)

print inc.probable_IAP.probable_income()
