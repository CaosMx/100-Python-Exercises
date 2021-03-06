"""
Exercise 24 - Iterate Dictionary

Question: Pa has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]ease complete the script so that it prints out the expected output.

    d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

Expected output: 

    b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    a has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Hint: Iterate through the d.items()  (Python 3) or d.iteritems()  (Python 2) with a for loop.
"""
# SOLUTION:

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
print(d)
# Vemos los resultados:
# {'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 'c': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]}
# Necesitamos "formato -> print" y realizar una "iteración -> for" para [KEY + VALUE] usando d.items(), por lo tanto:
for key, value in d.items():
    print(key, "has value", value)

"""
a has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
"""