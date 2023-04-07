N,B=map(int,input().split())
res,c=[],35
while N>0:
    if N<=B**(c+1):
        ch=0
        for i in range(B):
            if N>=(B-i)*(B**(c)):
                N-=(B-i)*(B**(c))
                res.append(str(B-i) if B-i<10 else chr((B-i)+55))
                ch=1
                break
        if ch!=1 and len(res)!=0:
            res.append('0')
        c-=1
    else:
        c-=1 
for i in range(c+1):
    res.append('0')
print(*res,sep='')