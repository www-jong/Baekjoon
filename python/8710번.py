k,w,m=map(int,input().split())
res=0
while k+res*m<w:
    res+=1
print(res)