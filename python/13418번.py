import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
N,M=map(int,input().split())

li=[]

for i in range(M+1):
    a,b,c=map(int,input().split())
    li.append([a,b,c])

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

li.sort(key=lambda x:x[2])
nodes=[i for i in range(N+1)]
res1,res2=0,0
for x,y,val in li:
    if find(x)!=find(y):
        res1+=val
        union(x,y)
nodes=[i for i in range(N+1)]
for x,y,val, in li[::-1]:
    if find(x)!=find(y):
        res2+=val
        union(x,y)

print((N-res1)**2-(N-res2)**2)