#mautheosach
'''n=int(input('nhap chieu dai list '))
a=[0]*n
for i in range(n):
    a[i]=int(input('nhap so '))
print(a)
for j in range(n-1,0,-1):
    for i in range(j):
        if a[i]>a[i+1]:a[i],a[i+1]=a[i+1],a[i]
for i in range(n):
    print(a[i],end=' ')'''
#test
a=list(map(int,input('nhap cac so ').split()))
print(a)
for j in range(len(a)-1,-1,-1):
    for i in range(j):
     if a[i]>a[i+1]:a[i],a[i+1]=a[i+1],a[i]
print(a)