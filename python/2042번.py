import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
li=[0]
sums=0
def one(b,c):
    global sums
    sums-=li[b]
    sums+=c
    li[b]=c

def two(b,c):
    tmp=0
    if c-b+1<n:
        tmp=sum(li[b:c+1])
    else:
        tmp=sums-li[1:b+1]-li[c:]
    print(tmp)

for i in range(n):
    li.append(int(input()))
sums=sum(li)
for i in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        one(b,c)
    else:
        two(b,c)
