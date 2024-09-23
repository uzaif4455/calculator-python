#functions in python
def gmean(a,b):
    mean=(a+b)/(a*b)
    print(mean)

def isgreater(a,b):
    if a > b:
        print("first no is greater")
    else:
        print("second is greater")
a=int(input("enter the number:"))
b=int(input("enter the number:"))
gmean(a,b)
isgreater(a,b)
c=int(input("enter the number:"))
d=int(input("enter the number:"))
gmean(c,d)
isgreater(c,d)