import sys,math
input=sys.stdin.readline
n,m=map(int,input().split())
li=[0]+list(map(int,input().split()))
sums,ex=[0]*(n+1),{}
sums[1]=li[1]
ex[li[1]%m]=1
count=0
for i in range(2,n+1):
    sums[i]=sums[i-1]+li[i]
    if sums[i]%m in ex:
        ex[sums[i]%m]+=1
    else:
        ex[sums[i]%m]=1
count=ex[0] if 0 in ex else 0
for i in ex.keys():
    count+=math.comb(ex[i],2)
print(count)

''''
누적합 구하기-> m으로 나눴을때 같은 나머지를 가지는 누적합들 분류
-> m으로나눴을때 나머지가 x인 누적합 인덱스 2개 i,j가 있을때,
i+1부터 j까지의 합은 나머지가 0이다.
그냥 누적합이 나머지가 0이면 그것도 카운트하는데, 개별로도 카운트
'''