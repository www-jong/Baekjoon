import sys
input=sys.stdin.readline
N=int(input())
li=[0]+[int(input()) for _ in range(N)]+[0]
stk=[]
res=-1
stk.append((0,li[1]))
for i in range(2,N+2):
    
    while stk and li[i]