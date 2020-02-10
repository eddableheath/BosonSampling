# An attempt to sample from lattices using Boson sampling
# Author: Edmund Dable-Heath
# Collecting data from sampling the lattices stored in the lattice directory:
# Dimension/ latt number/ 0 - 3, lattice bases, 4 shortest vector, 5 shortest vector length
# First test using 2 dimensional lattices, so 2 photons, 4 dimensional unitaries and pick 4 times per pick.

from Simulation import Sim
import numpy as np
import Unitaries as un
import math


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


print(np.linalg.norm(sum([sampler(2, np.genfromtxt('Lattices/2/0/0.csv', delimiter=',', dtype=None),
              np.genfromtxt('Unitaries/4/0.csv', delimiter=',', dtype=None)) for i in range(4)])))


def lattice_data(dimension, samples, number_unitaries=100, number_lattices=3, lattice_type='all'):
    """
    For a given dimension will pick from n different lattices, with basis type prescribed, using m different
    unitaries, sampling r times each time.
    :param dimension: dimension of lattice, int
    :param samples: number of samples, int
    :param number_unitaries: how many unitaries to test, default is all 100, int
    :param number_lattices: how many lattices to test, default/max is all 3 per dimension, int
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
    sample_number = 2 * dimension
    # how many photons: unitary_dimension = poly(photons), so round down square root of unitary dimension.
    photons = math.floor(math.sqrt(unitary_dimension))
    # retrieving unitaries
    unitaries = un.retrieval(dimension, number_unitaries)
    # Looping over lattices:
    if lattice_type == 'all':
        # loop over lattices
        lattices = [[np.genfromtxt('Lattices/' + str(dimension) + '/' + str(j) + '/' + str(i) + '.csv', delimiter=',', dtype=None)
                     for i in range(4)] for j in range(number_lattices)]
        short_vector = [np.genfromtxt('Lattices/' + str(dimension) + ',' + str(j) + '4.csv', delimiter=',', dtype=None)
                        for j in range(number_lattices)]
        short_vec_length = [np.genfromtxt('Lattices/' + str(dimension) + '/' + str(j) + '5.csv', delimiter=',', dtype=None)
                            for j in range(number_lattices)]
    else:
        lattices = [np.genfromtxt('Lattices/' + str(dimension) + '/' + str(j) + '/' + str(lattice_type) + '.csv', delimiter=',', dtype=None)
                    for j in range(number_lattices)]
        short_vector = [np.genfromtxt('Lattices/' + str(dimension) + ',' + str(j) + '4.csv', delimiter=',', dtype=None)
                        for j in range(number_lattices)]
        short_vec_length = [np.genfromtxt('Lattices/' + str(dimension) + '/' + str(j) + '5.csv', delimiter=',', dtype=None)
                            for j in range(number_lattices)]
        results = {}
        for u in unitaries:
            for l in range(len(lattices)):
                lengths = [np.linalg.norm(sum([Sim.Sim(photons, dimension, u)
                                               for i in range(sample_number)])) for i in range(samples)]

