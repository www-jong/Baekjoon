li=list(map(int,input().split()))
res=1
while True:
    cnt=0
    for i in li:
        if res%i==0:
            cnt+=1
    if cnt>2:
        print(res)
        break
    res+=1