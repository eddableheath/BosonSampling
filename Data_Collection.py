# Collecting Data for Boson Sampling
# Author: Edmund Dable-Heath
# This is where the actual processing of my data will be done.

import LatticeSampling as ls
import csv
import time

start_time = time.time()

results = {}
for lattice in range(4):
    new_latt_time = time.time()
    dimension_results = {}
    for dim in range(2, 13):
        new_dim_time = time.time()
        dimension_results[dim] = ls.lattice_data(dim, 1000, lattice)
        print('Done with dimension {} for lattice {}'.format(str(dim), str(lattice)))
        print('--- %s seconds ---' % (time.time() - new_dim_time))
    results[lattice] = dimension_results
    print('Done with lattice type {} -------------'.format(str(lattice)))
    print('--- %s seconds ---' % (time.time() - new_latt_time))



print('Results:------------------')
print(results)
print('--- %s seconds ---' % (time.time() - start_time))



w = csv.writer(open('Lattice_Sample_data_2.csv', 'w'))
for key, val in results.items():
    w.writerow([key, val])