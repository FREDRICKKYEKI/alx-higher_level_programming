#!/usr/bin/python3
"""

module that has the lazy_matrix_multiply function
that multiplies 2 matrices

"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):

    """Function that multiply 2 matrices
    Args:
        m_a (list): matrix a
        m_b (list): matrix b

    Returns:
        result of the multiplication

    """
    return np.matmul(m_a, m_b)
