import sys
n=list(sys.stdin.readline().strip())
cur=len(n)
for i in range(int(sys.stdin.readline())):
    c=list(map(str,sys.stdin.readline().strip().split()))
    if len(c)==2:
        n.insert(cur,c[1])
        cur+=1
    else:
        if c[0]=="L":
            cur-=(1 if cur>0 else 0)
        elif c[0]=="D":
            cur+=(1 if cur<len(n) else 0)
        else:
            if cur!=0:
                n.pop(cur-1)
                cur-=1
print(*n)

'''
abcd


'''