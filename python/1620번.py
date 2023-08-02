import sys
input=sys.stdin.readline
N,M=map(int,input().split())
name={}
num={}
for i in range(1+N):
    po=input().rstrip()
    name[po]=i
    num[i]=po
for i in range(M):
    tmp=input()
    if tmp.isnumeric():
        print(num[tmp])
    else:
        print(name[tmp])