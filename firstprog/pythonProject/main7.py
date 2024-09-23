#if-else in pthon
#var1=2
#var2=7
#var3=int(input())
#here int is taken because we want a integer value from user,if int is not mentione it will take as string
#if var3>var2:
 #   print("greater")
#else:
 #   print("lesser")
 #write a program to take input from user for their age if its greater then 18 they can drive,
#if less they cannot, and if equal to 18 we cant decide
"""print("enter your age?")
age=int(input())
if age<18:
    print("you cant drive")
elif age==18:
    print("i cant decide")

else:
    print("you can drive")"""

#write a program to take input from user for their age if its greater then 18 they can drive,
#if less they cannot, and if equal to 18 we cant decide and show not a valid age above 100
age=int(input("enter your age: "))
if age>18 and age<100:
    print("you can drive")
elif age==18:
    print("we cant decide,come and have physical test for driving")
else:
    print("not a valid age")