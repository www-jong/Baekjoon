import sys
input=sys.stdin.readline
def rounds(x):
    return round(x+0.000001)
n=int(input())
if n!=0:
    li=[0]
    for i in range(n):
        li.append(int(input()))
    li.sort()
    print(rounds(sum(li[1+rounds(n*0.15):n+1-rounds(n*0.15)])/(n-rounds(n*0.15)*2)))
else:
    print(0)