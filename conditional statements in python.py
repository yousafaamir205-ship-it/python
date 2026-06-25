#conditional statment

# age=int(input("enter your age: "))
# if(age>18):
#     print("eligible for license")
# elif(age==18):#elif statement is only runned only when if statement is false
#     print("eligible as you turned 18")
# else:
#     print("not eligible!")

#practice question
# marks=int(input("enter your marks: "))
# if(marks>=90):
#     print("grade is A")
# elif(90>marks>=80):
#     print("grade is B")
# elif(80>marks>=70):
#     print("grade is C")
# elif(70>marks):
#     print("Grade if D")

#nesting
# age=10
# name="ali"
# if(age==10):
#     if(name=="ali"):
#         print("found em")
#     else:
#         print("lost em")

#practise 1
number=int(input("enter a number"))
if(number%2==0):
    print("number is even")
else:
    print("number is odd")

#practise 2
n1=int(input("enter first number: "))
n2=int(input("enter second number: "))
n3=int(input("enter third number: "))
if(n1>n2 and n1>n3):
    print("first number is greatest")
elif(n2>n1 and n2>n3):
    print("second number is greatest")
else:
    print("third njmber us greatest")

#practise 3
n4=int(input("enter a number to check whether divisible by 7 or not"))
if(n4%7==0):
    print("divisible by 7")
else:
    print("not divisible by 7")