#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Napisz funkcję euclidean_distance obliczającą odległość między
dwoma punktami przestrzeni trójwymiarowej. Punkty są dane jako
trzyelementowe listy liczb zmiennoprzecinkowych.
np. odległość pomiędzy punktami (0, 0, 0) i (3, 4, 0) jest równa 5.
"""

def euclidean_distance(x, y):
    return (((y[0] - x[0]) ** 2) + ((y[1] - x[1]) ** 2) + ((y[2] - x[2]) ** 2)) ** (1/2)

input  = [[2.3, 4.3, -7.5], [2.3, 8.5, -7.5]]
output = 4.2

print(euclidean_distance(input[0], input[1]))