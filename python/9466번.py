import sys
sys.setrecursionlimit(10 ** 9)
input=sys.stdin.readline
def dfs(x):
    visit[x]=1
    nodes.append(x)
    if not visit[li[x]]:
        dfs(li[x])
    else:
        check(x)

def check(x):
    global res
    if li[x] in nodes:
        res-=len(nodes[nodes.index(li[x]):])

for i in range(int(input())):
    n=int(input())
    res=n
    li=[0]+list(map(int,input().split()))
    visit=[1]+[0]*(n)
    for i in range(1,n+1):
        if visit[i]==0:
            nodes=[]
            dfs(i)
    print(res)