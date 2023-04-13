import sys
input=sys.stdin.readline
N,M=map(int,input().split())
li=[]
nodes=[i for i in range(N+1)]
for i in range(M):
    li.append(list(map(int,input().split())))

def find(a):
    if nodes[a]==a:
        return a
    else:
        nodes[a]=find(nodes[a])
        return nodes[a]
    
def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        if a<b:
            nodes[b]=a
        else:
            nodes[a]=b
li.sort(key=lambda x:x[2])

cnt=0
res=0
i=0
max_v=-1
while cnt<N-1:
    a,b,v=li[i][0],li[i][1],li[i][2]
    if find(a)!=find(b):
        cnt+=1
        res+=v
        max_v=max(max_v,v)
        union(a,b)
    i+=1
print(res-max_v)