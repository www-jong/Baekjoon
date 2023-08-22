a,b=map(int,input().split())
r=1
for i in range(a,b+1):
    t=0
    for j in range(1,i+1):
        t+=j
    r*=t
print(r%14579)