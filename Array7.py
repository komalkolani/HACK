# -*- coding: utf-8 -*-
# Check if given array is Monotonic
def isMonotonic(A):
	x, y = [], []
	x.extend(A)
	y.extend(A)
	x.sort()
	y.sort(reverse=True)
	if(x == A or y == A):
		return True
	return False


# Driver program
B = [6, 5, 1, 8]

# Print required result
print(isMonotonic(B))
