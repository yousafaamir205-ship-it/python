#functions
# def sum(a,b):
#     s=a+b
#     print(s)
#     return s

# sum(2,3)

# def fun():
#     print("hello")

# def fun1(a,b,c):
#     print((a+b+c)/3)

# fun1(1,2,3)


#function with default peramater , here print is 0 
# def mul(a=0,b=0):
#     print(a*b)

# mul()
#practise questions:
#practise 1
# b=[1,2,3,4,5]
# def pf(list):
#     for item in list:
#         print(item,end=" ")
# pf(b)

#practise 2
# def fun(val):
#     num = 1

#     for n in range(1, val + 1):
#         num = num * n

#     print(num)

# fun(3)

#recursion
# def show(d):
#     if(d==0):
#         return
#     print(d)
#     show(d-1)
# show(5)
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return fact(n-1)*n

# print(fact(2))


#practise 1


def fun(a):
    sum=0
    if(a==0):
        return 0
    return a+fun(a-1)
print(fun(2))

#practise 2

def add(list,index=0):
    if(index==len(list)):

        return
    print(list[index])
    add(list,index+1)
fruits=["apple","mango","leeche"]
add(fruits)