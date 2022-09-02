import sys
input=sys.stdin.readline
N,C=map(int,input().split())
li=sorted([int(input()) for _ in range(N)])

def func(li,start,end):
    while start<=end:
        mid=(start+end)//2
        now=li[0]
        count=1
        
        for i in range(1,len(li)):
            if li[i]>=now+mid:
                count+=1
                now=li[i]
        if count>=C:
            global ans
            start=mid+1
            ans=mid
        else:
            end=mid-1

start=1
end=li[-1]-li[0]
ans=0
func(li,start,end)
print(ans)

'''
시작값과 끝값은 최소, 최대거리로 잡음
공유기의 간격을 이진분할함
처음은 절반으로 시작해 C보다 설치한 수가 적으면 거리를 다시 이진분할
C보다 설치한 수가 많으면 거리를 이진분할 해 조금 더 늘림

'''