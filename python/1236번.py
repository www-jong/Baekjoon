N,M=map(int,input().split())
li=[]
x=[1]*(N)
y=[1]*(M)
for i in range(N):
    S=input()
    for j in range(M):
        if S[j]=='X':
            x[i]=0
            y[j]=0
print(max(sum(x),sum(y)))