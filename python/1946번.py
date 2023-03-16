import sys
input=sys.stdin.readline
for _ in range(int(input())):
    N=int(input())
    li=[]
    res=1
    for i in range(N):
        a,b=map(int,input().split())
        li.append([a,b])
    li.sort()
    mins=li[0][1]
    for a,b in li:
        if mins>b:
            mins=b
            res+=1
    print(res)