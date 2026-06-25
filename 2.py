

#strings
# str1="this is ' a string. \t we are creating it in python."
# #\t for tab space, and \n for new line

# print(str1)

#concatination (joining two strings)

# str1="Muhammad"
# str2="yousaf"
# str= str1+" "+str2# this is how to add space in between strings
# print(str)
# #to find length of string

# print(len(str))

#indexing

# string="yousaf bhai"
# print(string[0])
# print(string[1])
# string2 =string[2]
# print(string2)
#we cant change characterlike string[1]=o

#slicing(accessing part of string)
# string="yousaf"
# print(string[0:len(string)])
# #we can also do
# print(string[0:])
# #and
# print(string[:len(string)])
# # negative indexing can also be done like list elemnt is -1 and second last is -2 and so on...
# str="apple"
# print(str[-3:-1])

#functions
# end with check wether main string last part end with the sub string
#str="i am studying python"
# print(str.endswith('t'))# t is substring here

# capitalized function (it create new string)

# print(str.capitalize())


# # replace function

# print(str.replace("o","a"))# replaces o with a here
# print(str.replace("python","c++"))#replaces pyhton with c++


#find function returns address of first occurance of character/ word if it doesnot exist, it return s -1
# print(str.find("o"))

# # count occurnce of word/ elemnt
# print(str.count("o"))

#practise question
# name=input("enter your name: ")
# print(len(name))
# practise 2
str="hi ##"
print(str.count("#"))