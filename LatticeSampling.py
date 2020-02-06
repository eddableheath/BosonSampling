# An attempt to sample from lattices using Boson sampling
# Author: Edmund Dable-Heath
# Collecting data from sampling the lattices stored in the lattice directory:
# Dimension/ latt number/ 0 - 3, lattice bases, 4 shortest vector, 5 shortest vector length
# First test using 2 dimensional lattices, so 2 photons, 4 dimensional unitaries and pick 4 times per pick.

from Simulation import Sim
import numpy as np
import Unitaries as un
import math


def sampler(dimension, samples, number_unitaries=100, number_lattices=3, lattice_type='all'):
    """
    For a given dimension will pick from n different lattices, with basis type prescribed, using m different
    unitaries, sampling r times each time.
    :param dimension: dimension of lattice, int
    :param samples: number of samples, int
    :param number_unitaries: how many unitaries to test, default is all 100, int
    :param number_lattices: how many lattices to test, default is all 3 per dimension, int
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
