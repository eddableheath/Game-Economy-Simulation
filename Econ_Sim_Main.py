##----------------------------------------------------------------------------##
##                            Economy Simulation                              ##
##----------------------------------------------------------------------------##

## Main File -------------------------------------------------------------------

# Imports
import numpy as np
import scipy as sp
import Econ_Sim_Expenditure as exp

black_hole = exp.spend_item('black_hole', 1500, 0.25, 1)

#print black_hole.probable_use()
#print black_hole.probable_spend()

cloak = exp.spend_item('Invisibility_cloak', 125, 0.5, 3)

#print cloak.probable_use()
#print cloak.probable_spend()

radar = exp.spend_item('radar', 200, 0.6, 3)

print radar.probable_spend()
print cloak.probable_spend()
print black_hole.probable_spend()
