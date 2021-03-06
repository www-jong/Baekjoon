'''
2xn 직사각형을 1x2, 2x1, 2x2로 채우는 방법이다.

d[1]=1개 : |
d[2]=3개 : || = ㅁ
d[3]=5개 : ||| |= |ㅁ , =| ㅁ|
dp[4]=11개 : |||| ||= ||ㅁ , |ㅁ| |=| ㅁ|| ㅁㅁ ㅁ= =|| == =ㅁ
...
대충 정리하자면
d[i]는 d[i-1]만큼 타일을 깔고 2x1 타일을 붙이는 방법
       d[i-2]만큼 타일을 깔고 1x2 타일을 2개까는 방법
       d[i-2]만큼 타일을 깔고 2x2 타일을 1개 까는 방법
즉, d[i]=d[i-1]+d[i-2]*2 가 된다.

는 말인데, 좌우에 까는 방법은 왜 고려대상이 아닌지 모르겠다 
왠만한 블로그에서는 전부, 베껴썼는지 피보나치언급만 하므로 정리해본다
좌우가 바뀌는 경우를 고려하지 않는 이유는, d[i-1] 또는 d[i-2]*2 이 부분에서
좌우가 바뀐 경우가 포함되어 있기 때문. 이론적으로 떠올리기는 힘들지만, 암튼 바뀜..?

'''

n=int(input())
d=[0]*(n+1)
d[1]=1
if n>1:
    d[2]=3
for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]*2
print(int(d[n]%10007))