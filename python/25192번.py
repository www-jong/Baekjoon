N=int(input())
dic={}
ch=0
res=0
for i in range(N):
    S=input()
    if S=='ENTER':
        res+=len(dic)
        #print(dic)
        dic={}
    elif S not in dic:
        dic[S]=1
#print(dic)
res+=len(dic)
print(res)