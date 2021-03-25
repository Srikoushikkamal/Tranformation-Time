n=int(input())
l,x,l1,r1,fin=[],[],[],[],0
for i in range(n):
    l.append(int(input()))
r=l[::-1]
ins=int(input())
for i in range(ins):
    x.append(int(input()))
opl,opr=0,0
for i in range(len(x)):
    for j in range(len(l)):
        if(x[i]>l[j]):
            l1.append(l[j])
            opl+=1
        else:
            l[j-1]=x[i]
            opl+=1
            break
    opl+=len(l1)
    '''for j in range(len(l)):
        if(l[j].isnumeric()):
            l1.append(l)'''
    print(l1)
    #Right
    '''for j in range(len(r)):
        if(x[i]<r[j]):
            r1.append(r[j])
            opr+=1
        else:
            r[j-1]=x[i]
            opr+=1
            r1.append(r[j-1:len(r)])
            break
    opr+=len(r1)'''
    mini=min(opl,opr)
    print(mini)
#fin+=mini
#print(fin)
