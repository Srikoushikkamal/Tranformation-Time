#00:05:07,400-234-090
#00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090
dict1={}
class Solution:
    def __init__(self,num):
        self.num=num
    def calc(self):
        hh=self.num[:2]
        mm=self.num[3:5]
        ss=self.num[6:8]
        self.num=self.num.split(",")
        numb=self.num[1]
        hh=int(hh)
        hh*=3600
        mm=int(mm)
        ss=int(ss)
        if(hh>300):
            hh/=60
            print(hh,mm)
            sums=(hh+mm)*150
        elif(mm*60>=300):
            sums=(mm+1)*150
        else:
            mm*=60
            sums=mm+ss
        print()
        if numb not in dict1:
            dict1[numb]=sums
        else:
            numb=str(numb)
            dict1[numb]=sums
            #dict1[numb].append(sums)
        #print(dict1)
        #print(max(dict1))

if __name__=="__main__":
    n=input().split("n")
    for i in n:
        if(len(i)==21):
            c=Solution(i[0:len(i)-1])
        else:
            c=Solution(i[0:len(i)])
        if(len(i)==21 or len(i)==20):
            c.calc()
        else:
            print("Wrong Format")
    l=[]
    for i in dict1:
        maxi=min(dict1)
        if(maxi<i):
            l.append(i)
    print("Bill:"dict1[l[0]])