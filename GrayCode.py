# Gray code generation for laplace expansion module for Boson sampling simulation
# Author: Edmund Dable-Heath
#
# The gray code needs to be generated for the space {-1,1}^n and the first element is required to be 1
# This generates gray codes not found and stores them in the directory GrayCodes

import os
import numpy as np

# For Gray code gen
def GrayCodeGen(n):
    """
    :param n: Dimension of Gray code
    :return: generates n by 2^n-1 array of {-1,1}^2n-1 with first entry 1 in Gray Code ordering
    """
    n = n - 1
    if n <= 0:
        return
    arr = [[1], [-1]]
    i = 2
    while True:
        if i >= 1 << n:
            break
        for j in range(i - 1, -1, -1):
            arr.append(arr[j])
        for j in range(i):
            arr[j] = [1] + arr[j]
        for j in range(i, 2*i):
            arr[j] = [-1] + arr[j]
        i = i << 1
    for k in range(len(arr)):
        arr[k] = [1] + arr[k]
    return arr


# Searching for and retrieving or writing Gray Code:
def RetrieveCode(k):
    """
    :param k: Desired Gray Code dimension
    :return: Required Gray code array, will generate and write code if not already available
    """
    # Code search
    def findcode(n):
        if any(str(n) in entry for entry in os.listdir('GrayCodes/')):
            return True
        else:
            return False
    # Special case for k = 1
    if k == 1:
        return np.array([[1]])
    else:
        if findcode(k) == True:
            return np.genfromtxt('GrayCodes/' + str(k) + '.csv', delimiter = ',')
        else:
            newCode = np.asarray(GrayCodeGen(k))
            np.savetxt('GrayCodes/' + str(k) + '.csv', newCode, delimiter = ',')
            return newCode

