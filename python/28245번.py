N=int(input())

def bitcount(n):
    if n==0:
        return 0
    return n%2+bitcount(n//2)

for i in range(N):
    M=int(input())
    if M==1:
        print(0,0)
        continue
    tmp,tmp2=M,M
    print(bin(M),len(bin(M)))
    co=bitcount(M)
    ch=0
    idx=0
    if co==1:
        idx=len(bin(M))-4
        print(idx, idx)
        continue
    while co>=3:
        if M&(1<<idx):
            M&=~(1<<idx)
            co-=1
        idx+=1
    print(bin(M))
    res=[]
    for j in range(len(bin(M))-2):
        if M&(1<<j):
            res.append(j)
    if len(res)==2:
        print(res[0],res[1])
    else:
        print(0,0)