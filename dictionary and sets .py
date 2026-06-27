#dictionary(bulitin)
#works like pairs
#word is key and meaning is value, keys cant be duplicate
# info={
#     "key":"value",
#     "name" : "yousaf",
#     "age":"21",
#     "marks": 32,
#     "subjects":["python","c++"],
#     "topics":("dictionary","sets"),
#     22:1
# }
# print(info)
# print(type(info))
# print(info["age"])# accessing with key
# print(info[22])
# info["name"]="amir"#changing values in dictionary
# info["surname"]="ali"#new index in dictionary
# print(info["name"])
# print(info["surname"])
# nulldic={}#empty dictionary
# print(type(nulldic))
# nulldic["1"]=2
# print(nulldic)

#nested dictionary

student={
    "name":"y1",
    "subjects":{
        "physics":"12",
        "math":"32"
    }

}
# print(student)#print main dictionary
# print(student["subjects"])#print data of child dictionary
# print(student["subjects"]["math"])#prints specific within subjects


#methods in dictionary
#keys return keys of dictionary
# print(student.keys())
# print(list(student.keys()))
# print(len(student))
# #values return all values of dictionary
# print(student.values())
# print(list(student.values()))
# #items returns key values tuples like () as pairs
# print(student.items())
#get reurn key values
# print(student["name"])
# print(student.get("name"))#preferable is this one bcz it doesnot give error if invalid index is given and if error occurs , all remaining code would not be executed
# #update add new value to the dictionary
# student.update({1:3,"ali":"ahmed"})
# print(student)


#SETS, stores unique values, it has not order and is immutable it caanot have list and dictonary

# collection={1,2,3,4,1.1}

# print(collection)
# print(type(collection))
# print(len(collection))

c1=set()#empty set
# print(type(c1))

#functionc
#add, remove
#set is mutable but eelemnts is immutable
c1.add(1)
c1.add(2)
c1.add(3)
print(c1)
c1.remove(1)
print(c1)
#clear empty the set
# c1.clear()
# print(c1)
#pop removes random values
print(c1.pop())
#union
c2={1,2,3,4}
print(c1.union(c2))
#intersection
print(c1.intersection(c2))
#practise 1
dictionary={
    "Cat":"a small animal",
    "table":["a peice of furniture","list of facts and figures"]

}
print(type(dictionary["table"]))


#practise2
list1={"python","java","c++","javascript","java","pyhton","java","c++","c"}
print(len(list1))

#practise3
dic={}
x=input("enter physics:")
dic.update({"physics marks:":x})

x=input("enter chemistry")
dic.update({"chemistry: ":x})
print(dic)

#practise 2
set={1,"1.0"}
print(set)