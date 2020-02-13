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

adj_lengths = [x / shortest_vec for x in lengths]


#distances = [np.linalg.norm(sum([ls.sampler(4, np.genfromtxt('Lattices/4/0/0.csv', delimiter=',', dtype=None),
#                                            np.genfromtxt('Unitaries/8/0.csv', delimiter=',', dtype=None))
#                                for i in range(8)])/shortest_vec) for j in range(10000)]

print('regular lengths ------------')
print('minimum', min(lengths))
print('maximum', max(lengths))
print('mean', st.mean(lengths))
print('mode', st.mode(lengths))
print('median', st.median(lengths))
print('ratio lengths --------------')
print('minimum', min(adj_lengths))
print('maximum', max(adj_lengths))
print('mean', st.mean(adj_lengths))
print('mode', st.mode(adj_lengths))
print('median', st.median(adj_lengths))
print('shortest vector', np.genfromtxt('Lattices/4/0/5.csv', delimiter=',', dtype=None))

fig1, ax1 = plt.subplots()
ax1.set_title('Lengths')
ax1.boxplot(lengths)

fig2, ax2 = plt.subplots()
ax2.set_title('Ratio')
ax2.boxplot(adj_lengths)
plt.show()