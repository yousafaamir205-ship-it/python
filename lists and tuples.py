#lists
# marks=[94.1,90,55,65.1,99,1]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(len(marks))
#we can also store elements of different types in list
# student=["yousaf",55,21,"lhr"]
# print(student)
#list can be changed and string cannot be changed in python
# str="hello"
# print(str[0])#string
# student[0]=3#list
# print(student)
# #slicing in lists
# print(student[:4])
# print(student[0:])
# #can also have negative index
# print(student[-3:-1])

#function for lists

list=[2,1,3]

# #append adds one elemtnt at last
# list.append(4)
# print(list)

# #sort sorts in ascending
# list.sort()
# print(list)

# #sorting in descending order
# list.sort(reverse= True)
# print(list)

#reverse function
# list.reverse()
# print(list)

# #insert at specific index
# list.insert(1,"YOUSAF")# 1 is index and yousaf is value
# print(list)

# #remove delete first occurance of element
# #pop works like remove
# list.pop(1)#removes element from 1st index
# print(list)
# list.remove(1)# removes first occurance of element in the bracket
# print(list)


#TUPLES

#creates imutable sequence of values just like string(values cant br changed)
# tup=(1,2,3,4)
# # print(type(tup))
# # print(tup[0])
# # #cannot assign element
# # t=()#empty tuple
# # t1=(1,)#this is how single valued tupled be created without , it would be its original type
# # #slicing in tuple
# print(tup[1:3])
# print(tup[-4:-1])

# #methods in tupke
# print(tup.index(2))
# print(tup.count(1))

#practise1
# v=[]
# m1=input("enter 3 favourite movies: ")
# m2=input("enter 3 favourite movies: ")
# m3=input("enter 3 favourite movies: ")
# v.append(m1)
# v.append(m2)
# v.append(m3)
# print(v)

#practise2
# list1=[12,13,13,12]
# c=list1.copy()
# c.reverse()
# if (list1==c):
#     print("palindrome")
# else:
#     print("not a palindrome")


    #practise 3
tup=("c","d","a","a","b","b","a")
print(tup.count("a"))
#practise 4

list1=["c","d","a","a","b","b",]
list1.sort()
print(list1)