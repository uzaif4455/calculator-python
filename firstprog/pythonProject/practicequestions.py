# to Add Two Numbers in Python
#1.1)
"""a=10
b=20
print(a+b)"""
#to take input from user and print two numbers
#1.2)
"""num1=int(input("enter the no 1:"))
num2=int(input("enter the no 2:"))
sum=float(num1)+float(num2)
print(sum)"""
#add two numbers using functions
#1.3)
"""def sum (a,b):
    return a+b
s=sum(10,11)
print(s)"""
# maximum of two numbers
#2.1)
"""a=int(input("enter no1:"))
b=int(input("enter the no :"))
if a>b:
    print("a is greater then b")
else:
    print("b is greater a ")"""
#2.2)
"""a=int(input("enter value for a :"))
b=int(input("enter value for b:"))
def max_1(a,b):
    return max(a,b)
m=max_1(a,b)
print(m)"""
#python program for factorial of a number
 #3.1)
"""def fact(n):
  if n==0 or n==1:
      return 1
  else:
      return n * fact(n-1)
print(fact(4))
print(fact(6))"""
#3.2)
""" 
n = int(input("Enter n:"))
fact = 1.
for i in range(2, n+1):
    fact = fact*i
print(f"Factorial of {n} is: {fact}")"""
#Python Program for Simple Interest
#Simple interest formula is given by: Simple Interest = (P x T x R)/100 Where, P is the principal amount T is the time and R is the rate
#4.1)
"""p=1000
t=5  #time in days
r=10   #rate of interest
simple_int=(p*t*r)/100
print(simple_int)"""
#4.2)
"""def simple_int(p,t,r):
     return (p*t*r)/100
print(simple_int(1000,5,10))"""
#Python program to interchange first and last elements in a lis
# def swap_list(new_list):
#5.1)
#     new_list[0],new_list[-1]=new_list[-1],new_list[0]
#     return new_list
# new_list=[1,2,3,4,5,34,67,89,9,64,3,2,42,100]
# print(swap_list(new_list))
#5.2)
def swapList(list):
    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0, last)  #ye zero wale element ko last me append karenga
    list.append(first)

    return list  
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))
#Python Program to Swap Two Elements in a List with 1st index to last and las to 2nd
#Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
#Output :[1 , 5 , 3 , 4 , 2]
"""def swap_case(n_list):
    n_list[1],n_list[4]=n_list[4],n_list[1]
    return n_list
n_list=[2,33,44,77,88]
print(swap_case(n_list))"""
#Check if element exists in list in Python
"""Check if an element exists in a list in Python
Using “in” Statement 
Using a loop 
Using any() function
Using count() function
Using sort with bisect_left and set()
Using find() method
Using Counter() function
Using try-except block
Check if an element exists in the list using the “in” statement
I"""
"""l=[1,2,3,4,5]
i=int(input())
if  i in l:
    print("the entered number is in list")
else:
    print("not in list")
"""


'''def element_exists(lst, element):
 try:
  lst.index(element)
  return True

 except ValueError:

  return False

test_list = [1, 6, 3, 5, 3, 4]

print(element_exists(test_list, 3))
print(element_exists(test_list, 7))
'''