#!/usr/bin/python3
"""0. Minimum Operations"""


def minOperations(n):
    """min operations"""
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor # H => Copy All => Paste => HH
            n //= divisor # operador de asignación de división entera
        divisor += 1
    
    return operations
