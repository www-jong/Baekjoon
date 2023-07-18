# 속도개선
import sys
input=sys.stdin.readline
N=int(input())
res=[0]*(N)
dic={}
squ=[]
for i in range(N):
    x1,y1,w,h=map(int,input().split())
    squ.append([x1,y1,w,h])

idx=0
for x1,y1,w,h in squ[::-1]:
    tmp=0
    for x in range(x1,x1+w):
        for y in range(y1,y1+h):
            if str(x)+'_'+str(y) not in dic:
                tmp+=1
                dic[str(x)+'_'+str(y)]=1
    res[idx]=tmp
    idx+=1
print(*res[::-1],sep="\n")