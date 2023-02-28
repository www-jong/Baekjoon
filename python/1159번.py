N=int(input())
dic={}
res=''
res2=''
for i in range(N):
    S=input()
    if S[0] not in dic:
        dic[S[0]]=1
    else:
        dic[S[0]]+=1
for k,v in dic.items():
    if v>=5:
        res+=k
res=sorted(res)
for i in res:
    res2+=i
print(res2 if len(res2)>=1 else "PREDAJA")