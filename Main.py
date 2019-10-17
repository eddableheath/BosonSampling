# Main File for Boson Sampling Simulation
# Author: Edmund Dable-Heath
# Implementation of algorithm B from https://arxiv.org/abs/1706.01260


from scipy.stats import unitary_group
import numpy as np
import random as rn


def BosonSampling(n, m, A):

    """
        Boson sampling simulation:
        n: number of photons
        m: number of input/output modes
        A: random unitary matrix from U(m)
        return: Photon output
    """

    # Instantiate empty r array
    r = []
    # Take first n rows of A
    A_n = A[:,:n]
    # Permute rows of A
    PA_n = A_n[:,rn.permutation(n)]
    # Make indexed weight
    w = []
    for row in range(0, m-1):
        w.append(abs(PA_n[row][0])**2)
    # Sample index from weighted index
    x = rn.choice(m, p=w)
    # Append to r
    r.append(x)
    # Laplace expansion
    for k in range(2,n):
        # Cut down to k columns and only take rows from r vals
        A_r = PA_n[r,:k]
        # Remove kth column
        B_k = np.delete(A_r,k,0)
