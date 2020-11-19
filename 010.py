"""

Exercise 10 - Sequence Item Picking

Question: Complete the script so that it prints out a list slice containing letters a, c, e, g, and i. 

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

Expected output: 

['a', 'c', 'e', 'g', 'i'] 

"""

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print (letters[0::2]) #-> Evens
print (letters[1::2]) #-> Odds

#['a', 'c', 'e', 'g', 'i']
#['b', 'd', 'f', 'h', 'j']

"""
The complete syntax of list slicing is [start:end:step] . 
When you don't pass a step, Python assumes the step is 1. 
[:]  itself means to get everything from start to end. 
So, [::2]  means get everything from start to end at a step of two.
"""
# 2 Puntos
