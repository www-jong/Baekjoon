import sys
n=sys.stdin.readline()
s=list(map(int,sys.stdin.readline().split()))
l={}
for i in s:
    if i in l:
        l[i]+=1
    else:
        l[i]=1
m=sys.stdin.readline()
def adds(x):
    if int(x) in l:
        return l[int(x)]
    else:
        return 0
l2=list(map(adds,sys.stdin.readline().split()))
print(*l2,sep=' ')