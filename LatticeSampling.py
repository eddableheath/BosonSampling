# An attempt to sample from lattices using Boson sampling
# Author: Edmund Dable-Heath
# Collecting data from sampling the lattices stored in the lattice directory:
# Dimension/ latt number/ 0 - 3, lattice bases, 4 shortest vector, 5 shortest vector length
# First test using 2 dimensional lattices, so 2 photons, 4 dimensional unitaries and pick 4 times per pick.

from Simulation import Sim
import numpy as np
import Unitaries as un
import math
import statistics as st
import time

# Measuring the time it will take
start_time = time.time()

def sampler(latt_dim, latt_basis, unitary):
    """
    Given a number of photons and a lattice in a certain dimension, return a single vector.
    :param latt_dim: dimension of the lattice (int), for photon number and BS dim.
    :param latt_basis: lattice basis (2 dimensional array)
    :param unitary: unitary for BS (2 dim array)
    :return: sampled vector (1 dim array)
    """
    return sum([np.append(latt_basis, -latt_basis, axis=0)[vec]
                for vec in Sim(math.floor(math.sqrt(2*latt_dim)), 2*latt_dim, unitary)])


#print(np.linalg.norm(sum([sampler(2, np.genfromtxt('Lattices/2/0/0.csv', delimiter=',', dtype=None),
#              np.genfromtxt('Unitaries/4/0.csv', delimiter=',', dtype=None)) for i in range(4)])))


def lattice_data(dimension, samples, lattice_type):
    """
    For a given dimension will pick from n different lattices, with basis type prescribed, using m different
    unitaries, sampling r times each time.
    :param dimension: dimension of lattice, int
    :param samples: number of samples, int
    :param lattice_type: which kind of basis to pick, default is to cycle through all of them, with the others:
    0: Original random basis, B_1
    1: B_2 = U * B_1 where U is a random unimodular matrix
    2: B_3 = LLL(B_1) LLL reduced B_1
    3: B_4 = U * B_3
    :return:
    """
    # how big the unitary should be
    unitary_dimension = 2 * dimension
    # how many times it needs to be sampled from per vector picked (just 2 * dimension for now)
    sample_number = 2
    # retrieving unitaries
    unitaries = un.retrieval(unitary_dimension, 100)
    # Looping over lattices:
    mins = []
    maxs = []
    means = []
    variances = []
    lattices = [(np.genfromtxt('Lattices/' + str(dimension) + '/' + str(i) + '/' + str(lattice_type) + '.csv', delimiter=',', dtype=None),
                 np.genfromtxt('Lattices/' + str(dimension) + '/' + str(i) + '/5.csv', delimiter=',', dtype=None)) for i in range(3)]
    for lattice in lattices:
        for u in unitaries:
            ratios = [x / lattice[1]
                      for x in [np.linalg.norm(sum([sampler(dimension, lattice[0], u)
                                                    for i in range(sample_number)])) for j in range(samples)]
                      if x != 0.0]
            mins.append(min(ratios))
            maxs.append(max(ratios))
            means.append(st.mean(ratios))
            variances.append(math.sqrt(st.variance(ratios)))
    return [st.mean(mins), st.mean(maxs), st.mean(means), st.mean(variances)]


#print(lattice_data(12, 1000, 0))
#print('--- %s seconds ---' % (time.time() - start_time))