N=int(input())
MAXS=4*(10**9)+1
li=[1]*(MAXS)
so=[]
for i in range(2,int(MAXS**0.5)):
    if li[i]:
        for j in range(i+i,MAXS,i):
            li[i]=0


for i in range(N):
    n=int(input())
    while True:
        if n==0 or n==1:
            print(2)
            break
        if li[n]:
            print(n)
            break
        else:
            n+=1