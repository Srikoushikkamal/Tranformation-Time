n=int(input())
n1=input()
l,l1=[],[]
for i in n1:
    if(i.isnumeric()):
        l.append(i)
add=0
feq=[]
for i in range(n+1):
    if(int(l[i+1]) not in feq):
        if(int(l[i])==0):
                add+=int(l[i+1])
                feq.append(int(l[i+1]))
    else:
        add-=int(l[i+1])

print("No. of Friends:",add)