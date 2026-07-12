text=input("enter a word: ")
countupper=0
countlower=0

for elemnts in text:
    if(elemnts.isupper()):
        countupper=countupper+1
    elif(elemnts.islower()):
        countlower=countlower+1
    
print("upper case elements: ",countupper)

print("lower case elements: ",countlower)
