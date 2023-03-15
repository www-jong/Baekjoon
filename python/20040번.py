import sys
input=sys.stdin.readline
n,m=map(int,input().split())
res=0
A_player={}
B_player={}
for i in range(m):
    a,b=map(int,input().split())
    if i%2==0:
        if a not in A_player:
            A_player[a]=b
        