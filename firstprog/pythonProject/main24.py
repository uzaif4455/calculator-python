#enumerate function in python
"""Enumerate function in python
The enumerate function is a built-in function in Python that allows you to loop over a sequence
(such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time.
 Here's a basic example of how it works:"""

#program example 1
'''marks=[19,36,66,88,90]
for index,mark in enumerate(marks):
    print(mark)
    if (index==3):
        print("awesome,uzaif")'''

#program example 2
'''fruits=["banana","apple","orange","apple"]
for index,fruit in enumerate(fruits):
    print(index,fruit)'''
#program 3(using of star in enumerate to edit the output)
"""marks=[56,66,78,99,85]
for index,mark in enumerate( marks, start=1):
    print(mark)
    if (index==3):
        print("awesome,uzaif")"""
