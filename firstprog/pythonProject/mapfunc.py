#map,filter and reduce function in python
"""def cube(x):
    return x*x*x

l1=[1,2,4,6]
new_l=[]
for item in l1:
    new_l.append(cube(item))
print(new_l)"""
   #or we can do with
"""def cube(x):
    return x*x*x
l1=[1,2,4,6,8]
new_l=[]
new_l=list(map(cube,l1))  #map  iss an higher order function as it takes function in it as an arguemnet
#   or
new_l=list(map(lambda x:x*x*x,l1))   # this does not need to define a function
print(new_l)
print(new_l)
def filter_func(a):
    return a>4
new_l2=list(filter(filter_func,l1))   #filter iss an higher order function as it takes function in it as an arguemnet

print(new_l2)
"""
"""from functools import reduce
numbers=[1,2,4,5,7]
# reduce higher order function hai ye pahle 1+2 karenga fir 2+4 fir 4+5 fir 5+7 final output 19 ayenga
def mysum(x,y):
    return x+y
sum=reduce(mysum,numbers)
print(sum)"""
