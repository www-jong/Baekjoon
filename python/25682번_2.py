# 시간초과!
import sys
input=sys.stdin.readline
N,M,K=map(int,input().split())
li=[[0]]
res=10**9
W_board=[[0]]
B_board=[[0]]

sum_w=[[0]*(M+1) for i in range(N+1)]
sum_b=[[0]*(M+1) for i in range(N+1)]

for i in range(K):
    W='0'+'WB'*((max(N,M)//2)+1)
    B='0'+'BW'*((max(N,M)//2)+1)    
    W_board.append(W if i%2==0 else B)
    B_board.append(B if i%2==0 else W)
for i in range(N):
    li.append('0'+input())

for i in range(1,N+1):
    for j in range(1,M+1):
        sum_w[i][j]=(1 if W_board[i][j]!=li[i][j] else 0)+sum_w[i][j-1]+sum_w[i-1][j]-sum_w[i-1][j-1]
        sum_b[i][j]=(1 if B_board[i][j]!=li[i][j] else 0)+sum_b[i][j-1]+sum_b[i-1][j]-sum_b[i-1][j-1]

for i in range(1,N-K+2):
    for j in range(1,M-K+2):
        W_retouch=(sum_w[i+K-1][j+K-1]-sum_w[i+K-1][j-1]-sum_w[i-1][j+K-1]+sum_w[i-1][j-1])
        B_retouch=(sum_b[i+K-1][j+K-1]-sum_b[i+K-1][j-1]-sum_b[i-1][j+K-1]+sum_b[i-1][j-1])
        res=min(res,W_retouch,B_retouch)
print(res)
'''
세로 N
가로 M

'''