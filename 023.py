"""
Exercise 23 - Multilevel Indexing

Question: Access the third value of key b  from the dictionary.

    from pprint import pprint
     
    d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

Expected output: 

13  

Hint: You need square brackets after square brackets here.

"""

from pprint import pprint
     
d = dict (a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
pprint (d)

# Imprimimos la lista y observamos que el valor que buscamos es 13, 
# Un tip es que parece matriz, por lo que podemos usar un formato tipo [][] 
# para imprimir el resultado:

"""
 KEY   VALUE IN POSITION:
 [ ]  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
 -------------------------------------
{'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
 'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
 'c': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]}
"""

pprint(d["b"][2])

# Otra forma:
pprint(d['b'][2])

# 13  -> 2 Puntos


