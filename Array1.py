# -*- coding: utf-8 -*-
"""
# Python 3 code to find sum
# of elements in given array


def _sum(arr):

	# initialize a variable
	# to store the sum
	# while iterating through
	# the array later
	sum = 0

	# iterate through the array
	# and add each element to the sum variable
	# one at a time
	for i in arr:
		sum = sum + i

	return(sum)


# driver function
arr = []
# input values to list
arr = [10, 3, 4, 14]

# calculating length of array
n = len(arr)

ans = _sum(arr)

# display sum
print('Sum of the array is ', ans)
