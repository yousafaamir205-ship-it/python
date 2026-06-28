# class Student:
#     collge="ABC"

#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def welcome(self):
#         print("welcome")


# s1=Student("yousaf",12)
# s1.welcome()

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print(sum/3)

# s1=Student("yousaf",[1,2,3])
# s1.avg()



#static methods

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     @staticmethod # static method
#     def hello():
#         print("hello")
#     def avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print(sum/3)

# s1=Student("yousaf",[1,2,3])
# s1.avg()
# s1.hello()



#Abstraction: hiding implementation details of class and show imp features
# class Car:
#     def __init__(self):
#      self.acc=False
#      self.brk=False
#      self.clutch=False   
#     def start(self):
#        self.clutch=True
#        self.acc=True
#        print("car started")
# c1=Car()
# c1.start()

#encapsulation: object having data and functions

#practise question1


class Account:
    def __init__(self,bal,num):
        self.balance=bal
        self.accnum=num
    def debit(self,amount):
        self.balance-=amount
        print(amount,"was debited")
        print(self.balance)

    def credit(self,amount):
        self.balance+=amount
        print(amount,"was credited")
        print(self.balance)
    

account1=Account(100000,123456)
account1.credit(1)