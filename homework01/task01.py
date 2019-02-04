#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Zad 2. Napisz funkcję even_elements zwracającą listę,
która zawiera tylko elementy z list o parzystych indeksach.
"""


## dla parzystych

def even_elements(input):
    score = numbers[1:10:2]
    return score

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_elements(numbers))

other_list = numbers


## dla nieparzystych

def other_elements(other_list):
    new_score = []
    for i in other_list:
        if not i%2 == 0:
            new_score.append(i)
    return new_score

print(other_elements(other_list))



#input = [1, 2, 3, 4, 5, 6]
#output = [1, 3, 5]
