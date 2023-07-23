N=int(input())
S=1
for i in range(1,N+1):
    S*=i
res=S//60//60//24//7
print(res)