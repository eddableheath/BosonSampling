# Test of boson sampling sim
# Author: Edmund Dable-Heath
# Hopefully this works...

from scipy.stats import unitary_group
import Main as bs


def Sim(n, m, U = 0):
    """
    Instantiating the boson sampling simulation
    :param n: number of photons
    :param m: number of input/output modes
    :param U: unitary matrix (optional input, will choose at random if not stated)
    :return: Photon output
    """
    # Generating m dimensional unitary matrix
    if U == 0:
        A = unitary_group.rvs(m)
        return bs.BosonSampling(n, m, A)
    else:
        return bs.BosonSampling(n, m, U)

#print(Sim(4, 4))

