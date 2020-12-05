"""
Exercise 22: Lists with range

Exercise for reference: 

Create a dictionary of keys a, b, c where each key has as value a list from 1 to 10, 11 to 20, and 21 to 30, respectively. 
Then print out the dictionary in a nice format.

Hint: Use a range function to create the lists

"""

d = {"a":list(range(1,11)), "b":list(range(11,21)), "c":list(range(21,31))}
print(d)

# {'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 'c': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]} 
# -> 2 Puntos



# Otra forma:

from pprint import pprint
     
e = {"a":list(range(1, 11)), "b":list(range(11, 21)), "c":list(range(21, 31))}
pprint(e)

# {'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
# 'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
# 'c': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]}


"""
Explanation: 

We're using ranges here to construct the lists. 
We're also using the built-in Python pprint  module, 
which is used to print out well-formatted views of datatypes in Python.
"""

"""
The syntax of the range() function is as follows:

Syntax:

range([start,] stop [, step]) -> range object

PARAMETER 	DESCRIPTION
start 	(optional) Starting point of the sequence. It defaults to 0.
stop (required) 	Endpoint of the sequence. This item will not be included in the sequence.
step (optional) 	Step size of the sequence. It defaults to 1.

"""
