import sys
n=sys.stdin.readline()
s=set(map(int,sys.stdin.readline().split()))
m=sys.stdin.readline()
l=list(sys.stdin.readline())
for i in range(len(l)):
    l[i]=s.count(l[i])