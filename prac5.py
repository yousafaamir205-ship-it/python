num=int(input("enter a number to reverse: "))
n=0
while(num!=0):
    digit=num%10
    n=n*10+digit
    num=num//10
print(n)
