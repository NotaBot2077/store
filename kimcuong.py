n=int(input("so le "))
n=n+2
for i in range(n,0,-1):
    if i%2!=0:print(int((i/2)-0.5)*" "+"*"*(n-i+1)+" "*int((i/2)-0.5))
n=n-2    
for i in range(n+2):
    if i%2!=0:print((int((i/2)-0.5)+1)*" "+"*"*(n-i+1)+" "*(int((i/2)-0.5)+1))