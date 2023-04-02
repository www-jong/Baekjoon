li=map(int,input().split())
res='S'
for i in li:
    if i!=0 and i!=1:
        res='F'
print(res)