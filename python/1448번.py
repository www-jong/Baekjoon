import sys
input=sys.stdin.readline
N=int(input())
li=[int(input()) for i in range(N)]
li.sort(reverse=True)
res=-1
for i in range(N):
    c=0
    g=0
    for j in range(i+1,N):
        for k in range(j+1,N):
            if li[i]<li[j]+li[k]:
                res=max(res,li[i]+li[j]+li[k])
                g=1
                break
            else:
                c=1
                break
        if c:
            break
    if g:
        break
print(res)