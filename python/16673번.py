C,K,P=map(int,input().split())
r=0
for i in range(C+1):
    r+=K*i+P*i*i
print(r)