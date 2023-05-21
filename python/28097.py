_=int(input())
res=0
li=list(map(int,input().split()))
for i in li:
    res+=i+8
res-=8
print(f'{res//24} {res%24}')
