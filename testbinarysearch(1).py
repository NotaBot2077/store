def binarysearch(lis,left,right,tar):
    if left>right:
        return -1
    mid=(left+right)//2
    if lis[mid]==tar:return mid
    elif lis[mid]>tar:return binarysearch(lis,left,mid-1,tar)
    else:return binarysearch(lis,mid+1,right,tar)
print(binarysearch([1,2,3,4,5,6,8,9,10],0,len([1,2,3,4,5,6,8,9,10])-1,10))