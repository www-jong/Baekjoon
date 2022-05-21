n,m=map(int,input().split())
l={}
for i in range(n):
    s=input()
    l[s]=i+1
    l[str(i+1)]=s
for i in range(m):
    print(l[input()])
    