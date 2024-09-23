name=input("enter your name:")
age=int(input("enter your age:"))
user_name=name + str(age)
print(user_name)
if age>18 and age<100:
    print("you can vote")
elif age>100:
    print("you can't vote,invalid input")
else:
    print("u can't vote,invalid input")
