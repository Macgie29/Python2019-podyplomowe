#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Napisz funkcję big_no zwracającej tzw. "Big 'NO!'"
(zob. http://tvtropes.org/pmwiki/pmwiki.php/Main/BigNo)
dla zadanej liczby tj. napis typu "NOOOOOOOOOOOOO!", gdzie liczba 'O' ma być
równa podanemu argumentem, przy czym jeśli argument jest mniejszy niż 5,
ma być zwracany napis "It's not a Big 'No!'".
"""

def big_no(n):
    if n < 5:
        print("It's not a Big 'No!'")
    else:
        print('N'+'O' * n + '!')
    pass

big_no(100)

input = 2
output = "It's not a Big 'No!'"
