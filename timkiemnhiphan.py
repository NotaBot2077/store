lis=list(map(int,input('nhap phan tu tang dan :').split()))
tar=int(input('nhap so can tim '))
dau=0
cuoi=len(lis)-1
while (dau<= cuoi):
    if tar in lis:
     giua=(dau+cuoi)//2
     if lis[giua]==tar:print('so can tim o vi tri',giua);break
     elif lis[giua]>tar:cuoi=giua-1
     else:dau=giua+1
    else:print('khong co');break