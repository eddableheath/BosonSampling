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
        sigma = standard_deviation / abs(R[i][i])
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
    Q, R = np.linalg.qr(Basis)
    bound = 2 ** (-dim)
    smooth = (1/math.pi) * math.sqrt(0.5 * math.log(2 * dim * (1 + (1/bound))))
    sizes = [np.linalg.norm(i) for i in Q.transpose()]
    return (smooth, smooth * max(sizes))


test_basis = np.array([[256, 0, 0],
                       [-101, 1, 0],
                       [-44, 0, 1]])
test_target = np.array([1, 1, 1])
test_std_dev = SmoothingParam(test_basis)[0]

result = KleinSampler(test_basis.transpose(), test_std_dev, test_target)
print(result)
print(np.linalg.norm(result))

q, r = np.linalg.qr(test_basis.transpose())
print(r)
