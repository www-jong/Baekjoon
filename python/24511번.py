from collections import deque
import sys
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
c=deque()
for i in range(N):
    if A[i]==0:
        c.append(B[i])
M=int(input())
M_li=list(map(int,input().split()))
res=[]
for x in M_li:
    c.appendleft(x)
    print(c.pop())