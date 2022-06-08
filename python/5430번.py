import sys
from collections import deque
ans=[]
for i in range(int(sys.stdin.readline())):
    p=sys.stdin.readline()
    check=sys.stdin.readline()
    check=0
    li=deque(eval(sys.stdin.readline()))
    for i in p:
        try:
            if i=="R":
                check=2 if check==0 else 0
            elif i=="D":
                if check==2:
                    li.pop()
                else:
                    li.popleft()
        except:
            check=1
            break
    if check==1:
        ans.append("error")
    else:
        f=""
        if check==2:
            for i in range(len(li)-1,-1,-1):
                f+=","+str(li[i])
        else:
            for i in range(len(li)):
                f+=","+str(li[i])
        ans.append("["+f[1:]+"]")
print(*ans,sep="\n")