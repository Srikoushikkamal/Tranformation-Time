n,num,f=int(input()),input().split(),int(input())
sq=1
num1=2
num2=0
sql=[]
le=len(num)
if(f>1):
    for i in num:
        sq*=2
        if(sq<len(num)):
            sql.append(sq)
    while(num2!=len(num)):
        for sq in sql:
            l=[]
            for i in range(sq):
                    l.append(num1)
                    num1+=1
            if(f in l):
                if(f>1):
                    print(l)
                    break
                else:
                    print(-1)
    num2+=1
else:
    print()
    print(-1)