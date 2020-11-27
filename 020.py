"""
Exercise 20 - Apply Function to Dictionary Items

Question: Calculate the sum of all dictionary values.

    d = {"a": 1, "b": 2, "c": 3}

Expected output: 

 6 
"""
d = {"a": 1, "b": 2, "c": 3}
e = d.values()
f = sum(e)
print (f)

#Otra forma:
print(sum(d.values()))

# 6 -> 2 Puntos

"""
Hint 1: First, use d.values()  to return an array with all dictionary values.
Hint 2: Apply the sum()  function to the returned array.

Explanation: 

d.values()  returns a list-like dict_values  object 
while the sum  function calculates the sum of the dict_values items.

"""
