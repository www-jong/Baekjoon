import sys
input=sys.stdin.readline
for i in range(int(input())):
    N=int(input())
    li=list(map(int,input().split()))
    d=[]
    for now in li:
        if len(d)==0:
            d.append([-now,0,0])
            continue
        