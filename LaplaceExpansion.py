# Laplace expansion module for boson sampling model
# Author: Edmund Dable-Heath
# Implementation of laplace expansion algorithm from https://arxiv.org/abs/1706.01260

import numpy as np
import random as rn

def LaplaceExpansion(B_k,k):

    """
    :param B_k: Reduced unitary matrix for permanent
    :param k: sequence marker
    :return: sequence of permanents of reduced matrices
    """

