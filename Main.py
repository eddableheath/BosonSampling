# Main File for Boson Sampling Simulation
# Author: Edmund Dable-Heath
# Implementation of algorithm B from https://arxiv.org/abs/1706.01260

import numpy as np
import LaplaceExpansion as lp


def BosonSampling(n, m, A):

    """
        Boson sampling simulation:
        n: number of photons
        m: number of input/output modes
        A: random unitary matrix from U(m)
        return: Photon output
    """
    # Take first n rows of A
    A_n = A[:,:n]
    # Permute rows of A
    PA_n = A_n[:,np.random.permutation(n)]
    # Make indexed weight
    w = [abs(PA_n[row][0]) ** 2 for row in range(0,m)]
    # Sample index from weighted index
    x = np.random.choice(m, p=w)
    # Append to r
    r = [x]
    # Laplace expansion
    for k in range(1, n):
        # Cut down to k columns and only take rows from r vals
        B_k = PA_n[r,:k+1]
        print('B_k', B_k)
        # Compute permanents of submatrices
        Perms = lp.LaplaceExpansion(B_k, k)
        print('Perms:', Perms)
        print(r)
        # weighted index
        weighted = []
        for i in range(m):
            print(i)
            sums = []
            for l in range(k+1):
                print('unitary value', PA_n[i][l])
                print('perm', Perms[l])
                print('value', PA_n[i][l] * Perms[l])
                sums.append(PA_n[i][l] * Perms[l])
            print('sums', sums)
            mod = abs(sum(sums))**2
            print('sum of sums', sum(sums))
            print('mod', mod)
            weighted.append(mod)
        #weighted = [
        #    abs(sum([PA_n[i][l] * Perms[l] for l in range(0, k)])) ** 2
        #    for i in range(0, m)
        #]
        print(weighted)
        print(sum(weighted))
        # Sample index from weighted index
        new_x = np.random.choice(m, p=weighted)
        # Append to r
        r.append(new_x)
    # Sort in non-decreasing order
    z = sorted(r)
    return z
