import random
dai=int(input('nhap chieu dai '))
rong=int(input('nhap chieu rong '))
k=int(input('nhap so nguyen k '))
tong=0
b=[[0]*dai for i in range(rong)]
for row in range(rong):
    for column in range(dai):
        b[row][column]=random.randint(0,300)-random.randint(0,300)
        if b[row][column]<k:tong=+b[row][column]
for row in range(rong):
    for column in range(dai):
        print("%4d"%b[row][column],end='')
    print()
print('tong la',tong)