#del keyword delete object or its properties

# class Student:
#     def __init__(self,name):
#         self.name=name
# s1=Student("yousaf")
# print(s1.name)
# del s1


#public, private

# class Account:
#     def __init__(self,acc_no,ac_pass):
#         self.acc_no=acc_no
#         self.__ac_pass=ac_pass#private krny k liay __lgana before name of attribute

# acc1=Account(123,1345)
# print(acc1.acc_no,acc1.ac_pass)

# class Person:
#     __name="yousaf"
#     def hello(self):

#         print(self.__name)

# p1=Person()
# print(p1.hello())

#inheritance and single iheritance
# class Car:
#     def start(self):
#         print("car started")

#     def stop(self):
#         print("Car stopped")
# class tcar(Car):
#     def __init__(self,name):
#         self.name=name
# car1=tcar("fortuner")
# car2=tcar("Grande")

# print(car1.name)
# print("car1 has",car1.start())
# print(car2.name)
# print("car2 has",car2.start())
# print(car1.stop())
# print(car2.stop())

#multi level inheritance

# class Car:
#     def start(self):
#         print("car started")

#     def stop(self):
#         print("Car stopped")
# class tcar(Car):
#     def __init__(self,brand):
#         self.brand=brand
# class fortuner(tcar):
#     def __init__(self,model):
#         self.model=model
# car1=fortuner("2018")
# car1.start()


#multiple inheritance
# class A:
#     var1="welcome class A"
# class B:
#     var2="wlecome to class B"
# class C(A,B):
#     var3="welcome to class C"
# varc=C()
# print(varc.var1)#class A attribute
# print(varc.var2)#class B attribute
# print(varc.var3)#class C attribute

#super method
# class Car:
#     def __init__(self,type):
#         self.type=type
#     def start(self):
#         print("car started")

#     def stop(self):
#         print("Car stopped")
# class tcar(Car):
#     def __init__(self,name,type):
#         self.name=name
#         super().__init__(type)
# car1=tcar("prius","electric")
# print(car1.type)

#class method

# class Person:
#     name="anonyms"
#     # def changename(self,name):
#     #     Person.name=name
#     @classmethod
#     def change_name(cls,name):#this change is done directly in class attribute
#         cls.name=name
# p1=Person()
# p1.change_name("yousaf")
# print(p1.name)
# print(Person.name)

#property decorator
# class Student:
#     def __init__(self,physics,chemistry,math):
#         self.physics=physics
#         self.chemistry=chemistry
#         self.math=math
#         # self.percentage=str((self.physics+self.chemistry+self.math)/3)#converting percentage in string
#     #it can be done as
#     @property
#     def percentage(self):
#         return str((self.physics+self.chemistry+self.math)/3)#converting percentage in string
#     #it can be done as
# stu1=Student(22,23,23)
# print(stu1.percentage)
# #changing marks should also change the percentage
# stu1.physics=98
# print(stu1.percentage)

#         #percentage



#polymorphim
#oprator overloading
# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def showNum(self):
#         print(self.real,"i +",self.img,"j")

#     def __add__(self,num2):
#         numreal=self.real+num2.real
#         numimg=self.img+num2.img
#         return Complex(numreal,numimg)
#     def __sub__(self,num2):
#         numreal=self.real-num2.real
#         numimg=self.img-num2.img
#         return Complex(numreal,numimg)


# num1=Complex(1,3)
# num1.showNum()
# num2=Complex(1,2)
# num1.showNum()
# print("addition")
# num3=num1+num2
# num3.showNum()

# print("subtraction")
# num3=num1-num2
# num3.showNum()


#practise1
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14 *self.radius**2
#     def per(self):
#         return 2*3.14*self.radius

# c1=Circle(21)
# print(c1.area())
# print(c1.per())

#practise2
class Employee:
    def __init__(self,role,dep,salary):
        self.role=role
        self.dep=dep
        self.salary=salary
    def showDetails(self):
        print("role is ", self.role)
        print("department is ", self.dep)
        print("salary is ", self.salary)
e1=Employee("hr manager","hr",300000)
e1.showDetails()