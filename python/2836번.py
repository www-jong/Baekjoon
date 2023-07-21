import sys
input=sys.stdin.readline

N,M=map(int,input().split())
li=[]
for i in range(N):
    a,b=map(int,input().split())
    if a<=b:
        continue
    li.append([a,b])

li.sort(key=lambda x:x[0])
res=M
x,y=li[0]
for x,y in li[1:]:
    