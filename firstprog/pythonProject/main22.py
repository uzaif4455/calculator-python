#raising custom error in python
"""n=int(input("enter number between 2 to 9:"))
if(n<2 or n>9):
    raise valueerror("value should be between 2 to 9!")
#for more custom errors refer on google (custom errors in python)
except:
    if str():"""

#program to show quit in value error execution
a = input("Enter any value between 5 and 9 : ")

if a == "quit":
    print("you choosed to quit")
elif (int(a) < 5 or int(a) > 9):
    raise ValueError("Value should be between 5 and 9")