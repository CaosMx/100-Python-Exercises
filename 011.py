"""

Create a script that generates and prints a list of numbers from 1 to 20. Please do not create the list manually.

"""

x = range(1,21)
print(list(x))

# Create a script that generates and prints a list of numbers from 1 to 20. Please do not create the list manually.
# 1 Punto
# El truco es castear el resultado com lista

"""
range()  is a Python built-in function that generates a range of integers. 
However, range()  creates a Python range object. 
To get a real list object, you need to use the list() function to convert the range object into a list object.
Syntax
range(start, stop, step)
"""