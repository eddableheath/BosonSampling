# An attempt to sample from lattices using Boson sampling
# Author: Edmund Dable-Heath
# Various different methods proposed for sampling from a lattice. Here we see vectors are picked from the E8 lattice
# given each output mode corresponding to a different basis vector.

from Simulation import Sim
import numpy as np

E8 = np.array([[2, -1, 0, 0, 0, 0, 0, 1/2],
               [0, 1, -1, 0, 0, 0, 0, 1/2],
               [0, 0, 1, -1, 0, 0, 0, 1/2],
               [0, 0, 0, 1, -1, 0, 0, 1/2],
               [0, 0, 0, 0, 1, -1, 0, 1/2],
               [0, 0, 0, 0, 0, 1, -1, 1/2],
               [0, 0, 0, 0, 0, 0, 1, 1/2],
               [0, 0, 0, 0, 0, 0, 0, 1/2]])

# Random unimodular matrices:
A = np.array([[7, 3, -12, -13, 77, -286, -1195, 5249],
              [5, 6, -23, 9, 92, -372, -1523, 6775],
              [3, -2, 4, -17, 11, -24, -116, 457],
              [-1, -4, 12, -12, -35, 150, 608, -2732],
              [-3, -1, 4, 7, -30, 109, 458, -2005],
              [-3, -4, 13, -6, -53, 212, 871, -3876],
              [2, -2, 7, -19, -3, 37, 129, -630],
              [-2, 3, -6, 17, -2, -10, -22, 151]])

X = np.matmul(A, E8)

picked = np.array([0, 0, 0, 0, 0, 0, 0, 0])
for i in Sim(4, 16):
    print('i:', i)
    z = (-1)**(i-1)
    if i % 2 == 0:
        j = i/2
        print(int(j))
        picked = picked + (z * E8[int(j)])
    else:
        j = (i - 1)/2
        print(int(j))
        picked = picked + (z * E8[int(j)])

print(picked)
print('length:', np.linalg.norm(picked))