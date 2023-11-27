N=int(input())
r=1
g=[0,0,0]
for i in range(N):
    g[i%3]+=1
    r+=sum(g)+1-g[i%3]
print(r)