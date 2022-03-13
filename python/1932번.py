n=int(input())
s=[0]*n
for i in range(n):
    s[i]=list(map(int,input().split()))
for i in range(n-2,-1,-1):
    for j in range(len(s[i])):
        s[i][j]=s[i][j]+max(s[i+1][j],s[i+1][j+1])
print(s[0][0])


# 가장 아래의 윗줄부터 거슬러 올라간다.
# s[i][j]는 아래의 두 수중 큰값의 합+자기자신의 합으로 재정의된다.
# 그렇게 맨위까지 거슬러 올라가면, 최대값이 나온다