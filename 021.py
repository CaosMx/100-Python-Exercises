"""
Exercise 21 - Dictionary Filtering

Question: Filter the dictionary by removing all items with a value of greater than 1.

    d = {"a": 1, "b": 2, "c": 3}

Expected output: 

{'a': 1}  

"""

d = {"a": 1, "b": 2, "c": 3}

# Creamos el diccionario donde vamos a guardar la info:
newDict = dict()
# Iteramos sobre los elementos del diccionario dado:
for (key, value) in d.items():
    #Condición de filtrado (Valores mayores a 1)
    if value <= 1:
        # Guardamos la info en nuevo diccionario:
        newDict [key] = value

print(newDict)

# Otra forma:
e =  {"a": 1, "b": 2, "c": 3}
e = dict((key, value) for key, value in d.items() if value <= 1)
print(e)



# {'a': 1} ->  2 Puntos

"""
Hint 1: Use dictionary comprehension.
Hint 2: Inside the dictionary comprehension access dictionary items with d.items()
if you are on Python 3, or dict.iteritems()  if you are on Python 2.
"""

"""

Explanation: 

Here we're using a dictionary comprehension. The comprehension is the expression inside dict(). 
The comprehension iterates through the existing dictionary items, and if an item is less or equal to 1, 
the item is added to a new dict. This new dict is assigned to the existing variable d, 
so we end up with a filtered dictionary in d.

"""
