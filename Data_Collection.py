# Collecting Data for Boson Sampling
# Author: Edmund Dable-Heath
# This is where the actual processing of my data will be done. For the time being will likely just be a test spot.

import LatticeSampling as ls
import numpy as np
import matplotlib.pyplot as plt
import statistics as st

shortest_vec = np.genfromtxt('Lattices/4/0/5.csv', delimiter=',', dtype=None)
lengths = [np.linalg.norm(sum([ls.sampler(4, np.genfromtxt('Lattices/4/0/0.csv', delimiter=',', dtype=None),
                                          np.genfromtxt('Unitaries/8/0.csv', delimiter=',', dtype=None))
                               for i in range(8)])) for j in range(1000)]
if 0.0 in lengths:
    lengths.remove(0.0)

#adj_lengths = lengths/shortest_vec THIS DOESN'T WORK LIKE THIS


#distances = [np.linalg.norm(sum([ls.sampler(4, np.genfromtxt('Lattices/4/0/0.csv', delimiter=',', dtype=None),
#                                            np.genfromtxt('Unitaries/8/0.csv', delimiter=',', dtype=None))
#                                for i in range(8)])/shortest_vec) for j in range(10000)]

print('minimum', min(lengths))
print('maximum', max(lengths))
print('mean', st.mean(lengths))
print('mode', st.mode(lengths))
print('median', st.median(lengths))
print('shortest vector', np.genfromtxt('Lattices/4/0/5.csv', delimiter=',', dtype=None))
fig1, ax1 = plt.subplots()
ax1.set_title('Test plot')
ax1.boxplot(lengths)
plt.show()