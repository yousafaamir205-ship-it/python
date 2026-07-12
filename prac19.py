list=[12,4,8,30,15]
secondLargest=list[0]
largest=list[0]
for elements in list:
    if elements>largest:
        largest=elements
    elif(elements>secondLargest and elements!=largest):
        secondLargest=elements

print(secondLargest)

