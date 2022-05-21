n=int(input())
N=set(map(int,input().split()))
m=int(input())
M=list(map(int,input().split()))
for i in range(len(M)):
    if M[i] in N:
        M[i]=1
    else:
        M[i]=0
print(*M)