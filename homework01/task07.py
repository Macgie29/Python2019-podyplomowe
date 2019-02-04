#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Napisz funkcję char_sum, która dla zadanego łańcucha zwraca
sumę kodów ASCII znaków. Wykorzystaj funkcję ord()
"""

def char_sum(text):
    score = sum(ord(ch) for ch in text)
    return score

input = "this is a string"
output = 1516

print(char_sum(input))
