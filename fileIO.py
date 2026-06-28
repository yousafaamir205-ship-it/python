#open read and close
# f=open("C:\\Users\\My PC\\Desktop\\main\\python\\2.py","r")
# print(f.read())
# print(f.readline())#read one line at a time
# f.close()

#append on a file
# f=open("try.txt","a")
# f.write("i am learning file handling")
# f.close()
# print("done")
#note: if i append or write a file and it doesnot exist, it would be created by itself

#with syntax
with open ("try.txt","r")as f:
    r=f.read()
    print(r)