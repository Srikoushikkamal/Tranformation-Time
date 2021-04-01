#input1:
#4
#2 0 1 0
#out: True

#input2:
#6
#3 0 0 2 0 0
#out:True


n,ind=int(input()),0
l=input().split()
for i in range(len(l)):
    new=int(l[i])
    if(new>0):
        if(new>0 and i==ind):
            ind=i+new
if((ind+1))==len(l):
    print(True)
else:
    print(False)