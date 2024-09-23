import flask
# please dont disturb this line
# print("hello world 6", end=",")
# print("\\my name is xyz")
#calculator
a=int(input("enter the no:"))
b=int(input("enter the no:"))
c=int(input("if c=1 then a+b,/if c=2 then a-b,/if c=3 then a/b,/if c=4 then a*b"))
if c==1:
    print(a+b)
elif c==2:
      print(a-b)
elif c==3:
      print(a/b)
elif c==4:
     print(a*b)

