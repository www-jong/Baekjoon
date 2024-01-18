import sys
input=sys.stdin.readline
N=int(input())
def lowerbound(tar,end):
    st=0
    while st<end:
        mid=(st+end)//2
        if tar<=res[mid][1]:
            end=mid
        else:
            st=mid+1
    return end

li=[]
li_r=set()
for i in range(N):
    a,b=map(int,input().split())
    li.append((a,b))
    li_r.add(a)
li.sort(key=lambda x:x[0])
res=[li[0]]
res_r=[0]
co=1

for i in range(1,N):
    if li[i][1]>res[-1][1]:
        res.append(li[i])
        res_r.append(co)
        co+=1
    else:
        now=lowerbound(li[i][1],co)
        res[now]=li[i]
        res_r.append(now)


#print([li[i][1] for i in range(N)])
#print(res_r)
co=co-1
g=[]
for i in range(N-1,-1,-1):
    if res_r[i]==co:
        co-=1
    else:
        g.append(li[i][0])
print(len(g))
print(*sorted(g),sep="\n")
