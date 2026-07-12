num=int(input("enter a number"))
num2=num
r=0
while (num!=0):
    digit=0
    digit=num%10
    r=r*10+digit
    num=num//10

if(num2==r):
    print("palindrome")
else:
    print("not a palindrome")