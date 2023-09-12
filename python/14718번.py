N,K=map(int,input().split())
enemy=[]
pl=[[],[],[]]
for i in range(N):
    a,b,c=map(int,input().split())
    enemy.append((a,b,c))
    pl[0].append(a)
    pl[1].append(b)
    pl[2].append(c)
pl[0].sort()
pl[1].sort()
pl[2].sort()
stat=[0,0,0]
res=10**9
for a in pl[0]:
    if a>res:
        break
    for b in pl[1]:
        if a+b>res:
            break
        for c in pl[2]:
            if a+b+c>res:
                break
            count=0
            for A,B,C in enemy:
                if A<=a and B<=b and C<=c:
                    count+=1
            if count==K:
                res=a+b+c
print(res)
