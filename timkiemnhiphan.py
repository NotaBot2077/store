'''<<<<<<< HEAD
lis=list(map(int,input('nhap so ').split()))
tar=int(input('nhap so can tim:'))
def binarysearch(lis,left,right,tar):
    if left>right:return -1
    mid=(left+right)//2
    if lis[mid]==tar:return mid
    elif lis[mid]>tar:return(binarysearch(lis,left,mid-1,tar))
    else:return(binarysearch(lis,mid+1,right,tar))
print('so can tim o vi tri',binarysearch(lis,0,len(lis)-1,tar))
'''
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