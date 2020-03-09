# Klein Sampler
# Author: Edmund Dable-Heath
# Klein sampler implementation for comparison to Boson sampler:

import numpy as np
import math

'Requires basis matrix to be column form.'

def KleinSampler(Basis, standard_deviation, target):
    '''
    Implementation of the Klein Sampler
    :param Basis: Basis matrix, n x m integer entries. n is lattice dim, m is space dim.
    :param standard_deviation: standard deviation of distribution
    :param target: mean of distribution
    :return: Returns sample from D_(Lamda(B), sigma, c)
    '''
    # Dimension of ambient space
    dim = len(Basis)
    # Dimension of lattice
    subdim = len(Basis[0])
    c = target
    # Initialise final vector with zeros
    v = np.zeros(dim)
    # Gram-Schmidt orthoganlisation:
    Q, R = np.linalg.qr(Basis, mode='reduced')
    # Transpose for numpy reasons
    Qt = Q.transpose()
    print(Qt)
    Bt = Basis.transpose()
    print(Bt)
    for i in range(subdim-1, -1, -1):
        print('iteration:', i, '-----------------')
        d = np.inner(c, Qt[i]) / (R[i][i] ** 2)
        print('shifty:', d)
        # Temporary standard deviation:
        sigma = standard_deviation / R[i][i]
        print('adjusted standard deviation:', sigma)
        # Randomised rounding via Gaussian:
        z = round(np.random.normal(loc=d, scale=sigma))
        print('sampled integer:', z)
        # Shifted target and final vector:
        c -= z * Bt[i]
        print('shifted target:', c)
        v += z * Bt[i]
        print('updated vec:', v)
    return v

def SmoothingParam(Basis):
    '''
    Approximates the smoothing parameter
    :param Basis: Lattice basis
    :return: Approximation of the lattice basis and lower bound on standard deviation
    '''
    dim = len(Basis)


test_basis = np.genfromtxt('Lattices/2/0/1.csv', dtype=None, delimiter=',')
test_target = np.array([0,0])
test_std_dev = 1.

print(KleinSampler(test_basis, test_std_dev, test_target))

