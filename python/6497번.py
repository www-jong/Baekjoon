import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000)
while True:
    m,n=map(int,input().split())
    if m==0 and n==0:
        break
    li=[]

    nodes=[i for i in range(m+1)]
    res=0
    for i in range(n):
        a,b,c=map(int,input().split())
        li.append([a,b,c])
        res+=c
    li.sort(key=lambda x:x[2])
    def find(a):
        if a==nodes[a]:
            return a
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
    tmp=0
    for i in range(n):
        a,b,v=li[i]
        if find(a)!=find(b):
            res-=v
            tmp+=v
            union(a,b)
    print(res)