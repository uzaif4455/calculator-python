"""Introduction to Loops
Sometimes a programmer wants to execute a group of statements a certain number of times.
 This can be done using loops. Based on this loops are further classified into following main
  types;

1)for loop
2)while loop
The for Loop
for loops can iterate over a sequence of iterable objects in python.
 Iterating over a sequence is nothing but iterating over strings, lists, tuples,
  sets and dictionaries."""

colors=("red","greeen","blue")
for color in colors:
    print(color)
    for i in color:
        print(i)
#range():
"""What if we do not want to iterate over a sequence? What if we want to use for loop for 
a specific number of times?

Here, we can use the range() function.

Example:
for k in range(5):
    print(k)"""

#for k in range(5):
 #   print(k)
#for k in range(1,20001,1000):
 #   print(k)


