# Test of boson sampling sim
# Author: Edmund Dable-Heath
# Hopefully this works...

from scipy.stats import unitary_group
import Main as bs

A = unitary_group.rvs(9)

Out = bs.BosonSampling(4, 9, A)

print(Out)
