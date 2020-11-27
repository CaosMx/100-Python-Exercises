
"""

Exercise 18: Find de Error

Exercise for reference: 

    d = {"Name": "John", "Surname": "Smith"}
    print(d["Smith"]) -> And Print Smith ¿?


"""

d = {"Name": "John", "Surname": "Smith"}
print (d["Surname"])

# Smith -> 1 Punto


"""
Answer: 

There is no key Smith  in the dictionary. Smith  is a value. You want to use Surname  if you want to access Smith :

print(d["Surname"])

Explanation: 

A KeyError always means Python could not find a key with the name shown next to KeyError (e.g. Smith ).

"""
