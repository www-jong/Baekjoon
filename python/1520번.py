import sys
input=sys.stdin.readline
M,N=int(input())
li=[[0]]
for i in range(M):
    li.append([0]+list(map(int,input().split())))
