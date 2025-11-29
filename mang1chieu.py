#1 bai 1
'''import random
n=int(input('nhap n='))
a=[0]*n
neg=pos=0
for i in range(n):
    a[i]=random.randint(0,300)-random.randint(0,300)
for i in a:
    if i<0:neg=neg+1
    else:pos=pos+1
print(a)
print('duong',pos)
print('am',neg)'''
#2 bai 2
'''
import random
dem=0
n=random.randint(8,10)
a=[0]*n
for i in range(n):
 a[i]=random.randint(0,10)
j=0
print(a)
for i in range(len(a)):
 if a[j]<a[i]:j=i
print(a[j],'',j)
'''
'''
#3 bai 3
dem=0
import random
n=random.randint(8,10)
a=[0]*n
for i in range(n):
 a[i]=random.randint(0,10)
print(a)
for i in range(len(a)-1,-1,-1):
 for j in range(i):
  if a[j]>a[j+1]:a[j],a[j+1]=a[j+1],a[j];dem+=1
print(a)
print(dem)
'''
#4 bai 4
import random
n=random.randint(8,10)
a=b=[0]*n
for i in range(n):
 a[i]=random.randint(0,10)
print(a)
a[0]=b[0]
for i in range(1,n):
 b[i]=b[i-1]+a[i]
print(b)