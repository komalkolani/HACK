# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 13:34:44 2022

@author: DELL
"""

# to use reduce function import reduce from functools
from functools import reduce


def find_remainder(arr, n):
	sum_1 = reduce(lambda x, y: x*y, arr)
	remainder = sum_1 % n
	print(remainder)


arr = [100, 10, 5, 25, 35, 14]
n = 11
find_remainder(arr, n)
