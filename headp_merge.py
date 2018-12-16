"""
input: 2 sorted list (the list item is required to be integer)
output: the smallest element to the largest elements

"""

import heapq

a = [1, 2, 6 ,8]
b = [2, 3, 7, 7, 13]
c = [1, 3, 4, 16]

def ascending(*args):
	for i in args:
		if not isinstance(i, list):
			print('An list input is required')
			raise TypeError
	for i in heapq.merge(*args):
		print(i)

# lesson learnt
# heapq.merge help to compare the first element of each list and emit the smallest out 
