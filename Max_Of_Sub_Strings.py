n=list(input())
l=[]
z=0
new1=str()
for i in range(len(n)):
    for j in range(i+1,len(n)+1):
        new=(n[i:j])
        new1=str()
        for k in new:
            if(k.isalpha()):
                new1+=str(k)
        l.append(new1)
l.sort()
feq=[]
for i in l:
    if(i not in feq):
        feq.append(i)
print(feq[-1])