# Test of boson sampling sim
# Author: Edmund Dable-Heath
# Hopefully this works...

from scipy.stats import unitary_group
import Main as bs

A = unitary_group.rvs(4)

Out = bs.BosonSampling(2, 4, A)

print(Out)


#for i in range(m):
        #    print(i)
        #    sums = []
        #    for l in range(k+1):
        #        print('unitary value', PA_n[i][l])
        #        print('perm', Perms[l])
        #        print('value', PA_n[i][l] * Perms[l])
        #        sums.append(PA_n[i][l] * Perms[l])
        #    print('sums', sums)
        #    mod = abs(sum(sums))**2
        #   print('sum of sums', sum(sums))
        #    print('mod', mod)
        #    weighted.append(mod)