import sys
dic={}
_=int(sys.stdin.readline())
def pri(x):
    if int(x) in dic:
        return 1
    else:
        return 0
for i in list(map(int,sys.stdin.readline().split())):
    if i not in dic:
        dic[i]=1
_=int(sys.stdin.readline())
li=list(map(pri,sys.stdin.readline().split()))
print(*li,sep="\n")