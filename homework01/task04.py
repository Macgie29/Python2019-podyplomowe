#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Napisz funkcję sum_from_one_to_n zwracającą sume liczb od 1 do n.
Jeśli podany argument jest mniejszy od 1 powinna być zwracana wartość 0.
"""

def sum_from_one_to_n(n):
    score = sum(range(n+1))
    return score

print(sum_from_one_to_n(4))

input = 999
output = 499500
