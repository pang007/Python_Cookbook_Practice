"""
Input: a nested list consisting of integers  -> list
Output: a flattened list consisting the element inside
"""

from collections import Iterable

nested_list = [1,[2,3,4],[5,6,7],[8,9]]

def flatten(nested_list, ignore_type = (str)):
	for item in nested_list:
		# str is an iterable so we have to check the item is not a str
		if isinstance(item, Iterable) and not isinstance(item, ignore_type):
			# as flatten is another iterable, hence we have to use yield from
			yield from flatten(item)
		else:
			yield item

for x in flatten(nested_list):
	print(x)

	
# yield from (a) where a is a iterable/ generator is equivalent to
# for i in a:
#	yield i
