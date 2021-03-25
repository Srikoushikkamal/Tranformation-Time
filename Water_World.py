days=int(input())
clus=int(input()) 
c,q,l=[],[],[]
for i in range(clus):
    new=input().split(" ")
    c.append(new[0])
    q.append(new[1])
    l.append(new[2])
print(l)
clus1=int(input())
add=0
c1=[]
m=[]
feq=[]
for i in range(clus1):
    new=input().split("_")
    ex=new[0]
    sec=new[1]
    z=int(sec[1])-1
    if('f' in ex):#len(new[0])==1):
        add+=int(l[z])
        c1.append(sec)
        print(c1)
    elif(int(l[z]))>=days*int(q[z]):
        add+=int(l[z])
    else:
        feq.append(ex)
        for j in range(z):
            print(l[j])
            m.append(ex)
            c1.append(sec)
            add+=int(l[j])
        add+=int(q[z])
    print(l)
print("\nSolution:",add)