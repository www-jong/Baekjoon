N=int(input())
li=[0]+list(map(int,input().split()))
for i in range(int(input())):
    gender,num=map(int,input().split())
    if gender==1:
        for j in range(num,N+1,num):
            li[j]=0 if li[j]==1 else 1
    else:
        idx=0
        li[num]=0 if li[num]==1 else 1
        while (num-idx>=1)and(num+idx<=N):
            if li[num-idx]==li[num+idx]:
                li[num-idx]=0 if li[num-idx]==1 else 1
                li[num+idx]=0 if li[num+idx]==1 else 1
            else:
                break
            idx+=1    
if N<=20:
    print(*li[1:])
else:
    for i in range(1,101,20):
        print(*li[i:i+20])