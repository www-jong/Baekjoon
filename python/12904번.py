import sys
sys.setrecursionlimit(100000)
S=input()
T=input()
res=0

while len(T)>=len(S):
    if T[-1]=='A':
        T=T[:len(T)-1]
    else:
        T=T[:len(T)-1][::-1]
    if T==S:
        res=1
print(res)