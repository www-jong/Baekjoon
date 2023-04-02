li=[0]*(10000)
li[1]=1
for i in range(2,10000):
    li[i]+=i+li[i-1]
while True:
    N=int(input())
    if N==0:
        break
    print(li[N])