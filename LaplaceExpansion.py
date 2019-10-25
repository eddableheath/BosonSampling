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
    :return: dictionary {j: v_j(delta)} where v_j(delta) is partial sum
    """
    sums = []
    for j in range(0, k):
        sum = 0
        for i in range(0, k-1):
            sum += B_k[i][j] * delta[i]
        sums.append(sum)
    return sums


# Forward partial product:
def ForwardPartialProd(PartSums, k):
    """
    :param PartSums: dictionary of partial sums
    :param k: sequence marker
    :return: dictionary {l: f_l(delta)} where f_l is forward partial product, f_1 = 1
    """
    FProds = {1: 1}
    for l in range(1, k):
        prod = 1+0j
        for j in range(0, l):
            print(j)
            prod *= PartSums[j]
            print('fprod:', prod)
        FProds[l+1] = prod
    return FProds


# Backward partial product:
def BackwardPartialProd(PartSums, k):
    """
    :param PartSums: dictionary of partial sums
    :param k: sequence marker
    :return: dictionary {l: b_l(delta)} where b_l is backward partial product, b_k = 1
    """
    BProds = {}
    for l in range(0, k-1):
        prod = 1+0j
        for j in range(l, k -1):
            print(j)
            prod *= PartSums[j]
            print('bprod:', prod)
        BProds[l+1] = prod
    BProds[k] = 1
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


def LaplaceExpansion(B_k, k):
    """
    :param B_k: Reduced unitary matrix for permanent
    :param k: sequence marker
    :return: sequence of permanents of reduced matrices
    """
    PartProds = PartialProducts(B_k, k)
    Perms = []
    for l in range(0, k):
        sum = 0
        count = 0
        for i in PartProds:
            sum += ((-1+0j)**count) * i[l]
            count += 1
        sum *= (1/(2**(k-2))) + 0j
        Perms.append(sum)
    return Perms