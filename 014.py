"""

Exercise 14 - Removing Duplicates

Question: Complete the script so that it removes duplicate items from the list a .

    a = ["1", 1, "1", 2]

Expected output: 

  ['1', 2, 1] 

"""

a = ["1", 1, "1", 2]
print (list(set(a)))

# ['1', 2, 1] -> 2 Puntos

"""

Dejándolo como Conjunto: {'1', 2, 1}
Para que tenga los paréntesis cuadrados hay que pasarlo a Lista despues de pasarlo a Conjunto para eliminar los duplicados.

"""

#Otras soluciones:

from collections import OrderedDict
b = ["1", 1, "1", 2]
b = list(OrderedDict.fromkeys(b))
print(b)

"""
Explanation 2:

Ordered dictionaries are another data type in Python that, unlike sets and normal dictionaries 
they preserve the order of the items. 
Here OrderedDict.fromkeys(a)  
would produce a OrderedDict  like [('1', None), (1, None), (2, None)] . 
Then we would convert that OrderedDict  to a list.
"""


c = ["1", 1, "1", 2]
d = []
for element in c:
    if element not in d:
        d.append(element)
print (d)

"""
Explanation 3:

This is another solution that would preserve the original order. 
We go through all the original list items and append them to the new list if they have not been appended before. 
The downside of this is that the operation can take a lot of time 
if the list as large as we need to access both lists and perform a conditional in each iteration.
"""

#[1, 2, '1']
#['1', 1, 2]
#['1', 1, 2]
