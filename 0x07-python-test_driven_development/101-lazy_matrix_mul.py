#!/usr/bin/python3
"""
 multiplies 2 matrices by using the module NumPy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiply 2 matrix
    Args:
        m_a: matrix 1
        m_b: matrix 2
    Returns:
        return m_a * m_b
    """
    return numpy.matmul(m_a, m_b)
