from copy import deepcopy
N,M=map(int,input().split())
li=[]
graph=[set([i]) for i in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)
res=0
res_li=[]
while min([len(graph[i]) for i in range(1,N+1)])!=N:
    tmp=0
    dic={}
    for a in range(1,N+1):
        now=len(graph[a])
        if now!=N:
            for x in graph[a]:
                if a not in dic:
                    dic[a]=graph[a].union(graph[x])
                else:
                    dic[a]=dic[a].union(graph[x])
            tmp+=len(dic[a])-now
    for k,v in dic.items():
        graph[k]=v
    res_li.append(tmp//2)
    res+=1
print(res)
print(*res_li,sep="\n")