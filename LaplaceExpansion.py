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
    B_kt = np.transpose(B_k)
    return [np.dot(B_kt[j], delta) for j in range(k+1)]


# Forward partial product:
def ForwardPartialProd(PartSums, k):
    """
    :param PartSums: dictionary of partial sums
    :param k: sequence marker
    :return: list of forward partial products
    """
    return [complex(1)] + [np.prod([PartSums[i] for i in range(l)]) for l in range(1,k+1)]


# Backward partial product:
def BackwardPartialProd(PartSums, k):
    """
    :param PartSums: dictionary of partial sums
    :param k: sequence marker
    :return: dictionary {l: b_l(delta)} where b_l is backward partial product, b_k = 1
    """
    return [np.prod([PartSums[j] for j in range(l, k-1)]) for l in range(0, k)] + [complex(1)]



# Partial products:
def PartialProducts(B_k, k):
    """
    :param B_k: reduced unitary matrix
    :param k: sequence marker
    :return: array [[f_1b_1(delta^1) ... f_k_b_k(delta^1)] ... [f_1b_1(delta^N) ... f_kb_k(delta^N)]] where N = 2^{k-1}
    """
    print("Partial Sum", PartialSum(B_k,k,[[1]]))
    print("Forward", ForwardPartialProd(PartialSum(B_k, k, [[1]]), k))
    print("Backward", BackwardPartialProd(PartialSum(B_k, k, [[1]]), k))


    return [[x*y
             for (x, y) in zip(ForwardPartialProd(PartialSum(B_k, k, delta), k), BackwardPartialProd(PartialSum(B_k, k, delta), k))
            ] for delta in gc.GrayCodes[k]]


def LaplaceExpansion(B_k, k):
    """
    :param B_k: Reduced unitary matrix for permanent
    :param k: sequence marker
    :return: sequence of permanents of reduced matrices
    """

    def SignAlt(n):
        return (-1 + 0j) ** n

    PartProds = PartialProducts(B_k, k)
    print('Part prods:', PartProds)
    return [
        (1 / (2 ** (k - 2))) + 0j * sum([
            SignAlt(n)*PartProds[n][l]
            for n in range(0,2**(k-1))
        ])
        for l in range(0,k)
    ]