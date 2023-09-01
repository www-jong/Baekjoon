import sys
input=sys.stdin.readline
N,M=map(int,input().rstrip().split())
keyword=set()
r=N
for i in range(N):
    keyword.add(input().rstrip())
for i in range(M):
    words=input().rstrip().split(",")
    for i in words:
        if i in keyword:
            r-=1
            keyword.discard(i)
    print(r)