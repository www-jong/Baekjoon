a,b=map(int,input().split())
fi=[0,1,1,2,3,5]
for i in range(500):
    fi.append((fi[-1]+fi[-2])%10)
r=''
for i in range(a,b+1):
    r+=str(fi[i%60])
print(r)