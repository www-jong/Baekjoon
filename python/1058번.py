N=int(input())
li=[[] for i in range(N)]
for i in range(N):
    S=input()
    for j in range(N):
        if S[j]=='Y':
            li[i].append(j)
res=0
for i in range(N):
    visit=[0]*N
    for j in li[i]:
        visit[j]=1
        for z in li[j]:
            visit[z]=1
    visit[i]=0
    res=max(sum(visit),res)
print(res)