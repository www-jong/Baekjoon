import sys
input=sys.stdin.readline
N=int(input())
li=list(map(int,input().split()))
li.sort()
res=[10**12,0,0]
st=0
end=N-1
while st<end:
    now=li[st]+li[end]
    if abs(res[0])>=abs(now):
        res=[now,li[st],li[end]]
    if now<0:
        st+=1
    elif now>0:
        end-=1
    else:
        res=[now,li[st],li[end]]
        break
print(min(res[1],res[2]),max(res[1],res[2]))