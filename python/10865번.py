import sys
input=sys.stdin.readline
N,M=map(int,input().split())
li=[0]*(N+1)
for i in range(M):
    A,B=map(int,input().split())
    li[A]+=1
    li[B]+=1
for i in range(1,N+1):
    print(li[i])