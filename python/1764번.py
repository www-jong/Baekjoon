import sys
n,m=map(int,sys.stdin.readline().split())
dic={}
se=[]
for i in range(n):
    n=sys.stdin.readline()
    dic[n]=1
for i in range(m):
    n=sys.stdin.readline()
    if n in dic:
        se.append(n)
print(len(se))
se.sort()
for i in se:
    print(i,end="")