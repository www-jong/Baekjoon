import sys
sys.setrecursionlimit(10 ** 9)
input=sys.stdin.readline
def dfs(li,x):
    global nodes
    visit[x]=1
    if not visit[li[x]]:
        dfs(li,li[x])
    else:
        check(x)

def check(x):
    global nodes,res
    if nodes[li[x]]==1:
        nodes[li[x]]=0
        check(li[x])
        res-=1
for i in range(int(input())):
    n=int(input())
    res=n
    li=[0]+list(map(int,input().split()))
    nodes=[1]*(n+1)
    nodes[0]=0
    visit=[0]*(n+1)
    for i in range(1,n+1):
        if nodes[i]==1:
            dfs(li,i)
    print(res)