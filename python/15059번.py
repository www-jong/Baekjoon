l=list(map(int,input().split()))
L=list(map(int,input().split()))
r=0
for i in range(3):
    r+=max(L[i]-l[i],0)
print(r)