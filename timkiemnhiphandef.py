def timkiemnhiphan(li,target):
    start=0;edt=len(li)-1
    while start<=edt:
     mid=(start+edt)//2
     if li[mid]==target: return mid
     elif li[mid]>target:edt=mid-1
     else:start=mid+1
a=[1,2,3,4,5]
print(timkiemnhiphan(a,3))