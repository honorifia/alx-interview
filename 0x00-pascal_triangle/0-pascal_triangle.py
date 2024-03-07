#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row
    """
    if n <= 0:
        return []

    # Memoization dictionary to store computed values of combinations
    memo = {}

    def combination(n, k):
        """
        Calculate the binomial coefficient C(n, k) using memoization
        """
        if k == 0 or k == n:
            return 1
        if (n, k) in memo:
            return memo[(n, k)]
        result = combination(n - 1, k - 1) + combination(n - 1, k)
        memo[(n, k)] = result
        return result

    triangle = [[combination(i, j) for j in range(i + 1)] for i in range(n)]
    return triangle
