#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Napisz funkcję days_in_year zwracającą liczbę dni w roku (365 albo 366).
"""

def days_in_year(year):
    if year % 4 == 0:
        days = 366
    elif year % 100 == 0:
        days = 365
    elif year % 400 == 0:
        days = 366
    else:
        days = 365
    return days

print(days_in_year(2020))

input = 2019
output = 365
