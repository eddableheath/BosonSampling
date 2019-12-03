# Test of boson sampling sim
# Author: Edmund Dable-Heath
# Hopefully this works...

from scipy.stats import unitary_group
import Main as bs


def Sim(n, m):
    """
    Instantiating the boson sampling simulation
    :param n: number of photons
    :param m: number of input/output modes
    :return: Photon output
    """
    # Generating m dimensional unitary matrix
    A = unitary_group.rvs(m)
    return bs.BosonSampling(n, m, A)

#print(Sim(4, 4))

