# #practise 1
# i=1
# while i<=100:
#     print(i)
#     i=i+1
# #practise 2
# n=100
# while n>=1:
#     print(n)
#     n=n-1
#practise 3
# n1=2
# n3=1
# while n3<=10:
#     print(n1,"*",n3,"=",n1*n3)
#     n3=n3+1
#practise 4
# list1=[1,4,9,26,35,36,49,64,81,100]
# n=0
# while n<len(list1):
#     print(list1[n])
#     n=n+1
#practise 5
# tup=(1,4,9,16,25,36,49,64,81,100)
# n=int(input("enter value to search: "))
# i=0
# while i<len(tup):
#     if n==tup[i]:
#         print("value found")
#         break
#     i=i+1
# else:
#     print("value was not found")

#break and continue
#break pe jha break wha loop khtm
#continue terminate current itearation and move to the next iteration
# i=0
# while i<=5:
    
#     if(i==3):
#         i=i+1
#         continue
#     print(i)
#     i=i+1
    #for loop
# list=[1,2,3]
# for num in list:
#      print(num)
# else:
#      print("done")#optional ahi yeh
# tup=(1,2,3,4)
# for num in tup:
#     print(num)

    #practise 1
# l1=[1,4,9,16,25,36,49,64,81,100]
# for num in l1:
#      print(num)
#practise 2
# l1=(1,4,9,16,25,36,49,64,81,100)
# x=49
# ind=0
# for num in l1:
#     if x==num:
#         print("value found ",ind)
        
#         break
#     ind=ind+1
# else:
#         print("value was not found")
#range function, start at 0 and step size 1

# for i in range(9):
#      print(i)
#     # range (start, stop, step size) stop size is necessory
# for i in range(1,5):#(start and stop)
#      print(i)
# for i in range(1,5,2): # (start, stop and increment/jjump)
#      print(i)

# #practise 1
# for i in range(101):
#      print(i)
# #practise 2
# for i in range(100,0,-1):
#      print(i)
# #practise 3
# n=int(input("enter numbe for table: "))
# for i in range(1,11,1):
#      print(n*i)


#practise 
# sum=0
# n=int (input("enter numbers to find sum: "))
# while n>=0:
#     sum=sum+n
    
#     n=n-1
# print(sum)
    #practise
n=int(input("enetr numbe rto find factorial: "))
num=1
for numb in range(n,1,-1):
    num=num*n
print(num)