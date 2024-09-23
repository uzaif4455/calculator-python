#exception handling in python
"""ry….. except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.

Syntax:
try:
     #statements which could generate
     #exception
except:
     #Soloution of generated exception"""
a=input("enter the number:")
print(f"the multiplication for number {a} is")
try:
    for i in range(1,12):
        print(f"{int(a)}x{i}={int(a)*(i)}")
except :
    print("invalid input!")


print("end of program")
