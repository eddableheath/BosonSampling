# Laplace expansion module for boson sampling model
# Author: Edmund Dable-Heath
# Implementation of laplace expansion algorithm from https://arxiv.org/abs/1706.01260

import numpy as np
import GrayCode as gc


# Partial sum:
def PartialSum(B_k, k, delta):
    """
    :param B_k: B_k matrix - unitary missing k'th column
    :param k: sequence marker
    :param delta: delta from {-1,1}^{k-1} space
    :return: list of partial sums
    """
    sums = [
        sum([B_k[i][j] * delta[i] for i in range(0, k-1)])
            for j in range(0, k)
    ]
    return sums


# Forward partial product:
def ForwardPartialProd(PartSums, k):
    """
    :param PartSums: dictionary of partial sums
    :param k: sequence marker
    :return: list of forward partial products
    """
    FProds = [1]
    for l in range(1, k):
        prod = 1+0j
        for j in range(0, l):
            print(j)
            prod *= PartSums[j]
            print('fprod:', prod)
        FProds.append(prod)
    return FProds


# Backward partial product:
def BackwardPartialProd(PartSums, k):
    """
    :param PartSums: dictionary of partial sums
    :param k: sequence marker
    :return: dictionary {l: b_l(delta)} where b_l is backward partial product, b_k = 1
    """
    BProds = [
        np.prod([PartSums[j] for j in range (l, k-1)])
        for l in range(0, k-1)
    ]
    BProds.append(1)
    return BProds


# Partial products:
def PartialProducts(B_k, k):
    """
    :param B_k: reduced unitary matrix
    :param k: sequence marker
    :return: array [[f_1b_1(delta^1) ... f_k_b_k(delta^1)] ... [f_1b_1(delta^N) ... f_kb_k(delta^N)]] where N = 2^{k-1}
    """
    GrayCode = gc.GrayCodes[k]
    PartProds = []
    for delta in GrayCode:
        print('delta:', delta)
        PartSum = PartialSum(B_k, k, delta)
        print('Partial Sums:', PartSum)
        Forward = ForwardPartialProd(PartSum, k)
        print(Forward)
        Backward = BackwardPartialProd(PartSum, k)
        print(Backward)
        prods = []
        for l in range(1, k+1):
            prods.append(Forward[l]*Backward[1])
        PartProds.append(prods)
    return PartProds


def SignAlt(n):
    return (-1+0j)**n


def LaplaceExpansion(B_k, k):
    """
    :param B_k: Reduced unitary matrix for permanent
    :param k: sequence marker
    :return: sequence of permanents of reduced matrices
    """
    PartProds = PartialProducts(B_k, k)
    Perms = [
        (1 / (2 ** (k - 2))) + 0j * sum([
            SignAlt(n)*PartProds[n][l]
            for n in range(0,2**(k-1))
        ])
        for l in range(0,k)
    ]
    return Perms