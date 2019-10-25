# Gray code generation for laplace expansion module for Boson sampling simulation
# Author: Edmund Dable-Heath
#
# The gray code needs to be generated for the space {-1,1}^n and the first element is required to be 1
# Ideally this check a look up table and if it doesn't find the Gray code already generated it will generate it
#
# First pass: Manually enter Gray code


import numpy as np


# For Gray code gen
def GrayCode(n):

    """
    Gray code generation
    :param n: dimension
    :return: Gray code list
    """

    list = []



# Gray Codes
GC_1 = np.array([[1]])

GC_2 = np.array([[1, 1],
                 [1, -1]])

GC_3 = np.array([[1, 1, 1],
                 [1, 1, -1],
                 [1, -1, -1],
                 [1, -1, 1]])

GC_4 = np.array([[1, 1, 1, 1],
                 [1, 1, 1, -1],
                 [1, 1, -1, -1],
                 [1, 1, -1, 1],
                 [1, -1, -1, 1],
                 [1, -1, -1, -1],
                 [1, -1, 1, -1],
                 [1, -1, 1, 1]])

GC_5 = np.array([[1, 1, 1, 1, 1],
                 [1, 1, 1, 1, -1],
                 [1, 1, 1, -1, -1],
                 [1, 1, 1, -1, 1],
                 [1, 1, -1, -1, 1],
                 [1, 1, -1, -1, -1],
                 [1, 1, -1, 1, -1],
                 [1, 1, -1, 1, 1],
                 [1, -1, -1, 1, 1],
                 [1, -1, -1, 1, -1],
                 [1, -1, -1, -1, -1],
                 [1, -1, -1, -1, 1],
                 [1, -1, 1, -1, 1],
                 [1, -1, 1, -1, -1],
                 [1, -1, 1, 1, -1],
                 [1, -1, 1, 1, 1]])

GC_6 = np.array([[1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, -1],
                 [1, 1, 1, 1, -1, -1],
                 [1, 1, 1, 1, -1, 1],
                 [1, 1, 1, -1, -1, 1],
                 [1, 1, 1, -1, -1, -1],
                 [1, 1, 1, -1, 1, -1],
                 [1, 1, 1, -1, 1, 1],
                 [1, 1, -1, -1, 1, 1],
                 [1, 1, -1, -1, 1, -1],
                 [1, 1, -1, -1, -1, -1],
                 [1, 1, -1, -1, -1, 1],
                 [1, 1, -1, 1, -1, 1],
                 [1, 1, -1, 1, -1, -1],
                 [1, 1, -1, 1, 1, -1],
                 [1, 1, -1, 1, 1, 1],
                 [1, -1, -1, 1, 1, 1],
                 [1, -1, -1, 1, 1, -1],
                 [1, -1, -1, 1, -1, -1],
                 [1, -1, -1, 1, -1, 1],
                 [1, -1, -1, -1, -1, 1],
                 [1, -1, -1, -1, -1, -1],
                 [1, -1, -1, -1, 1, -1],
                 [1, -1, -1, -1, 1, 1],
                 [1, -1, 1, -1, 1, 1],
                 [1, -1, 1, -1, 1, -1],
                 [1, -1, 1, -1, -1, -1],
                 [1, -1, 1, -1, -1, 1],
                 [1, -1, 1, 1, -1, 1],
                 [1, -1, 1, 1, -1, -1],
                 [1, -1, 1, 1, 1, -1],
                 [1, -1, 1, 1, 1, 1]])

# Look up library:

GrayCodes = {1: GC_1,
             2: GC_2,
             3: GC_3,
             4: GC_4,
             5: GC_5,
             6: GC_6}

