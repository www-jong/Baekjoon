import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
N=int(input())

li=[]
nodes=[i for i in range(N+1)]
stars=[]
def find(a):
    if a==nodes[a]:
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

for _ in range(N):
    x,y=map(float,input().split())
    stars.append([x,y])

for i in range(N):
    for j in range(i+1,N):
        x1,y1=stars[i]
        x2,y2=stars[j]
        li.append([i,j,(abs(x1-x2)**2+abs(y1-y2)**2)**0.5])
li.sort(key=lambda x:x[2])

res=0
for x,y,val in li:
    if find(x)!=find(y):
        res+=val
        union(x,y)

print(res)