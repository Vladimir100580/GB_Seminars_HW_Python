i = set()
print(''.join(sorted('121')))
i.add(''.join(sorted('1231')))
i.add(''.join(sorted('1321')))
i.add('12')

print(i)


for i in range(5, -1, -1):
    print(i)


mas = []
mas.extend([7]*3)
mas.extend([9]*0)
print(mas)

li = ["5","0","","0",""]
for i in li:
    if i:
        print("yes")
    else:
        print("no")