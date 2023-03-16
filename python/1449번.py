N,L=map(int,input().split())
li=[0]+list(map(int,input().split()))
li.sort()
res=0
idx=1
while idx<=N:
    st=li[idx]
    if idx==N:
        res+=1
        break
    for i in range(idx+1,N+1):
        if li[i]-st+1>L:
            idx=i
            res+=1
            print(f'{idx} {res}')
            break
        elif i==N and li[i]-st+1<=L:
            idx=N
            break
print(res)
