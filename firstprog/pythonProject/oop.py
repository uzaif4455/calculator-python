#oop is done to map real world entity
#oop is user defined functions,here user can assign values, handle function as per need
"""class Student:#ye class hai
    college_name="abc college"
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def welcome(self):
        print("welcome student",self.name)
    def get_marks(self):
        return self.marks
s1=Student("joy",23,99)
print(s1.name,s1.age)
s1.welcome()
print(s1.get_marks())
s2=Student("rohan",33,77)
print(s2.name,s2.age)
s2.welcome()
pr
int(s2.get_marks())"""

#program question
# class Student:
#     def __init__(self,name ,marks):
#         self.name=name
#         self.marks=marks
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum +=val
#             print("hi", self.name ,"your average is:", sum/3)
# s1=Student("john",[98,99,97])
# s1.get_avg()
#abstraction in oops is hiding the implementation details of class and only showing
# the essential features to the user
#program to know abstraction inoops
"""class Cars:
    def __init__(self):
        self.acc= False
        self.brk=False
        self.clutch=False
    def start(self):
            self.acc=True   #here this lines are working as abstraction
            self.brk=True   #
            self.clutch=True  #
            print("your car has strarted!")
car1=Cars()
car1.start()"""
#polymorphism and overloadging
#"""program 1)
# class Complex():
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def show_numbers(self):
#         print(self.real,"i+",self.img,"j")
#
#     def __add__(self,num2):
#         newreal=self.real + num2.real
#         newimg=self.img + num2.img
#         return Complex(newreal,newimg)
#
#     def __sub__(self,num2):
#         newreal=self.real-num2.real
#         newimg=self.img-num2.img
#         return Complex(newreal,newimg)
#
#
# num1=Complex(1,3)
# num1.show_numbers()
#
# num2=Complex(4,6)
# num2.show_numbers()
#
# num3 =num1 + num2
# num3.show_numbers()


# class Complex():
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
#
#     def show_numbers(self):
#         print(f"{self.real} + {self.img}i")
#
#     def __add__(self, num2):
#         new_real = self.real + num2.real
#         new_img = self.img + num2.img
#         return Complex(new_real, new_img)
#
#     def __sub__(self, num2):
#         new_real = self.real - num2.real
#         new_img = self.img - num2.img
#         return Complex(new_real, new_img)
#
#
# num1 = Complex(1, 3)
# num1.show_numbers()
#
# num2 = Complex(4, 6)
# num2.show_numbers()
#
# num3 = num1 + num2
# num3.show_numbers()

#program
"""class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.radius

s1=Circle(21)
print(s1.area())
print(s1.perimeter())"""
#program for inheritance
"""class Employee():
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showdetails(self):
        print("role=",self.role)
        print("department=",self.department)
        print("salary=",self.salary)
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","IT","70000")

g1=Engineer("elon ","33")
print(g1.name,g1.age)
print(g1.showdetails())
"""
#dunder function in oops
'''class Order():
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self, ordr2):
        return self.price > ord2.price
ord1= Order("chips",20)
ord2= Order("biscuit",25)

print(ord1<ord2)'''

