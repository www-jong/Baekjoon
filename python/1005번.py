import sys
input=sys.stdin.readline
sys.setrecursionlimit(100000)
def func(x,visit,times,check): # x까지의 최소시간.
    if visit[x]:
        return times[x]
    t=[]
    for i in check[x]:
        times[i]=func(i,visit,times,check)
        visit[i]=1
        t.append(times[i])
    return max(t)+times[x]

for _ in range(int(input())):
    N,K=map(int,input().split())
    check=[[] for _ in range(N+1)]
    times=[0]+list(map(int,input().split()))
    visit=[1]*(N+1)
    for i in range(K):
        a,b=map(int,input().split())
        visit[b]=0
        check[b].append(a)
    w=int(input())
    print(func(w,visit,times,check))