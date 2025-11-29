#cach lam binh thuong
'''b=[[0]*10 for i in range(9)]
for row in range(9):
 for column in range(10):
  b[row][column]=(row+1)*(column+1)
for row in range(9):
 for column in range(10):
  print(b[row][column],end=' ')
 print()

b=[[(r+1)*(c*1) for r in range(10)] for c in range(10)]
for row in range(9):    
  for column in range(10):
   print(b[row][column],end=' ')
  print('')
'''
from numpy import
a=[[1,2,3]
   ,[4,5,6]
   ,[7,8,9]]
print(a.shape)