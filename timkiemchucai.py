cha=input('nhap chu cai ')
cha=cha.upper()
l=[0]*26
aphalbet=[]
for i in range(26):
    aphalbet+=[chr(ord('A')+i)]
for j in range(len(cha)):
    if cha[j] in aphalbet:
     l[ord(cha[j])-ord('A')]+=1#hàm trừ chữ cái xuất hiện đặt số lần xuất hiện vào trong list l 
for i in range(len(l)):
    if l[i]>0:
        print('chu',chr(ord("A")+i),'xuat hien',l[i])
print(l)