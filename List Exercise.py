listx =[12,13,14,16,19,18,23,26]

even = []
odd  = []

for item in listx:
    if item % 2 ==0:
        even.append(item)
    else:
        odd.append(item)

print('Even list = ',even)
print('Odd list = ',odd)

print('Hi')
