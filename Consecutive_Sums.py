n=int(input())
c=0
for i in range(1,n+1):
    sums=0
    for j in range(i,n):
        sums+=int(j)
        if(sums==n):
            c+=1
print(c)