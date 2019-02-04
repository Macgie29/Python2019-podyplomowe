#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Napisz funkcję common_chars(string1, string2), która zwraca alfabetycznie
uporządkowaną listę wspólnych liter z lańcuchów string1 i string2.
Oba napisy będą składać się wyłacznie z małych liter.
"""


def common_chars(string1, string2):
    set_1 = set(string1.lower())
    set_2 = set(string2.lower())
    output_set = []
    for a in set_1:
        if a in set_2 and a != ' ':
            output_set.append(a)
    output_set = sorted(output_set)
    return output_set


input1 = "this is a string"
input2 = "ala ma kota"
output = ['a', 't']

print(common_chars(input1, input2))
