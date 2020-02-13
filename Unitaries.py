# Generation and retrieving of unitary matrices for Boson sampling simulation
# Author: Edmund Dable-Heath
#
# This will generate 100 random unitary matrices and store them as CSVs in a directory to be found later.

import numpy as np
from scipy.stats import unitary_group
import os


# Generating unitaries for dimension d
def GenUnitary(d):
    """
    Generates 100 unitaries of dimension d and stores them in directory unitaries, labelled by dimension d
    :param d: dimension
    :return: unitaries
    """
    # Dimension search
    if any(str(d) in entry for entry in os.listdir('Unitaries/')):
        return
    else:
        path = 'Unitaries/' + str(d)
        os.mkdir(path)
        for i in range(0, 100):
            unitary = unitary_group.rvs(d)
            np.savetxt(path + '/' + str(i) + '.csv', unitary, delimiter=',')


# Retrieving unitary matrices
def retrieval(d, m):
    """
    Retrieving unitaries
    :param d: dimension
    :param m: number required
    :return: returns m unitaries of dimension d
    """
    # Dimension search
    if any(str(d) in entry for entry in os.listdir('Unitaries/')):
        return [np.genfromtxt('Unitaries/' + str(d) + '/' + str(i) + '.csv', delimiter=',', dtype=None)
                for i in range(0, m)]
    else:
        GenUnitary(d)
        return [np.genfromtxt('Unitaries/' + str(d) + '/' + str(i) + '.csv', delimiter=',', dtype=None)
                for i in range(0, m)]


#GenUnitary(8)
