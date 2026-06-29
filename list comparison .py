numbers=[i for i in range(5)]
print(numbers)

#priting squares

squares=[i*i for i in range(1,6)]
print(squares)

#printing even
even=[i for i in range(20)if i%2==0]
print(even)

#printing cube
cube=[i*i*i for i in range(3)]
print(cube)

#printing odd numbers
odd=[i for i in range(9)if i%2!=0]
print(odd)


#convert into upper case

words=["apple","mango"]
upper=[words.upper()for word in words]
print(words)