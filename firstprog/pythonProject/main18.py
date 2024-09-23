#Python docstrings are the string literals that appear right after the definition of a function,
# method, class, or module.
"""def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)"""
# #@*  (f-string in python)
letter = "my name is {0} and i am from {1}"
name ="uzaif"
country="india"
#print(letter.format(name,country))
print(f"my name is {name} and i am from {country}")
#program2 in f-string
txt="dollar price {price:.2f} dollars!"
print(txt.format(price=49.099999))