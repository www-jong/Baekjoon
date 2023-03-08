N=int(input())
li=[0]+list(map(int,input().split()))+[0]
ball_N=int(input())
ball=list(map(int,input().split()))
dp=[[0]*(15001) for i in range(N+1)]

def back(now,weight):
    if now>N or dp[now][weight]:
        return
    dp[now][weight]=1
    back(now+1,weight+li[now+1])
    back(now+1,abs(weight-li[now+1]))
    back(now+1,weight)

back(0,0)
for i in ball:
    ch=0
    if i>15000:
        print("N",end=" ")
    else:
        for j in range(1,N+1):
            if dp[j][i]==1:
                print("Y",end=" ")
                ch=1
                break
        if ch==0:
            print("N",end=" ")
        