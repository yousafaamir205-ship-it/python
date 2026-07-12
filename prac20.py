list=[1,2,2,3,4,4,5]

first=[]
for elements in list:
    if elements not in first:
        first.append(elements)
    
print(first)

        