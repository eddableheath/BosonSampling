# Main File for Boson Sampling Simulation

from scipy.stats import unitary_group
from numpy import np

def BosonSampling(n, m, A):

    """
        Boson sampling simulation:
        n: number of photons
        m: number of input/output modes
        A: random unitary matrix from U(m)
    """

    # Instantiate empty r array
    r = []
    # Take first n rows of A
    A_n = A[:,:n]
