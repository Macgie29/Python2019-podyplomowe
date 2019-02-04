#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Napisz funkcję sum_div35(n), która zwraca sumę wszystkich liczb podzielnych
przez 3 lub 5 mniejszych niż n.
"""

def sum_div35(n):
    numbers = list(range(n))
    right = []
    for i in numbers:
        if i < n and (i % 3 == 0 or i % 5 == 0): ## nie bylem pewien tego fragmentu pytania mniejsze niz n, wiec dodalem to i < n. Jeżeli to nie jest potrzebne, to ten fragment można usunąć :)
            right.append(i)
    score = sum(right)
    return score

print(sum_div35(1000))

input = 100
output = 2318

