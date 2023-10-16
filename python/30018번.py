N=int(input())
li=list(map(int,input().split()))
li2=list(map(int,input().split()))
r=0
for i in range(N):
    if li[i]<li2[i]:
        r+=li2[i]-li[i]
print(r)