A,B=map(int,input().split())
K,X=map(int,input().split())
r=min(K+X,B)-max(K-X,A)
print(r+1 if r>=0 else "IMPOSSIBLE")