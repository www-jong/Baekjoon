N,S=map(int,input().split())
li=list(map(int,input().split()))
st,end=0,0
sums=0
res=10**9
while True:
    if sums>=S:
        res=min(res,end-st)
        sums-=li[st]
        st+=1
    else:
        if end==N:
            break
        sums+=li[end]
        end+=1
print(0 if res==10**9 else res)
