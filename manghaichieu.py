'''b=[[(row+1)*(column+1) for row in range(10)] for column in range (9)]
for r in range(9):
    for c in range(10):
     print("%4d"%b[r][c],end=' ')
    print()
'''
'''
b=[[0]*10 for i in range(9)]
for row in range(9):
 for column in range(10):
  b[row][column]=(row+1)*(column+1)
for r in range(9):
    for c in range(10):
        print("%4d"%b[r][c],end='')
    print()
#tao mang hai chieu co 7 cot va 5 hang va in ra so be hon k
'''
k=int(input('nhap khoa k '))
b=[[0]*7 for i in range(5)]
'''[[1,2,3,4,5,6,7],
   [8,9,10,11,12,13,14],
   [15,16,17,18,19,20,21],
   [22,23,24,25,26,27,28],
   [29,30,31,32,33,34,35]
   ]
'''
dem=0
for row in range(5):
 for column in range(7):
  b[row][column]=int(input('nhap so'))
print(b)
for r in range(5):
    for c in range(7):
        if b[r][c]<k:print('so be hon k la',b[r][c]);dem=+1
if dem==0:print('khong co phan tu nao')