#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Zad 4. Napisz funkcje oov(text, vocab), która zwraca listę wyrazów
(bez duplikatów), które występują w tekście text i nie występują w liście
znanych wyrazów vocab. Argumenty funkcji text i vocab to odpowiednio łańcuch
znakowy i lista łańuchów znakowych (oov = out of vocabulary)
"""
input = "this is a string , which i will use for string testing"
vocab = [',', 'this', 'is', 'a', 'which', 'for', 'will', 'i']

def oov(text, vocab):
    words = text.split(' ')
    rest = []
    for i in words:
        if i not in vocab:
            rest.append(i)
    func_set = set(rest)
    score = list(func_set)
    return score

print(oov(input, vocab))

input = "this is a string , which i will use for string testing"
vocab = [',', 'this', 'is', 'a', 'which', 'for', 'will', 'i']
output = ['string', 'testing', 'use']
