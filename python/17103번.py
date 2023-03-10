max=1000001
li=[1]*(max)
so=[]
dic={}
for i in range(2,max):
    if li[i]:
        for j in range(i*i,max,i):
            li[j]=0
        so.append(i)
        dic[i]=1
T=int(input())
for _ in range(T):
    N=int(input())
    res=0
    for i in so:
        if i>N//2:break
        if N-i in dic:
            res+=1
    print(res)