n=int(input())
ar=[]
res=[]
for i in range(n):
    g,h=map(int,input().split())
    ar.append([g,h])
for i in range(n):
    a=1
    for j in range(n):
        if ar[i][0]<ar[j][0] and ar[i][1]<ar[j][1]:
            a+=1
    res+=[a]

print(*res)
