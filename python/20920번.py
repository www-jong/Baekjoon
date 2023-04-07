import sys
input=sys.stdin.readline
N,M=map(int,input().rstrip().split())
dic={}
for i in range(N):
    s=input().rstrip()
    if len(s)>=M:
        if s in dic:
            dic[s]+=1
        else:
            dic[s]=1
sor=[]
for v,k in dic.items():
    sor.append([k,len(v),v])
sor.sort(key=lambda x:(-x[0],-x[1],x[2]))
for i in range(len(sor)):
    print(sor[i][2])