import sys
ans=[]
for i in range(int(sys.stdin.readline())):
    p=sys.stdin.readline()
    check=sys.stdin.readline()
    li=eval(sys.stdin.readline())
    check=0
    for i in p:
        try:
            if i=="R":
                check=2 if check==0 else 0
            elif i=="D":
                li.pop(-1 if check==2 else 0)
        except:
            check=1
            break
    if check==1:
        ans.append("error")
    else:
        f=""
        for i in range(len(li)):
            f+=","+str(li[len(li)-1-i if check==2 else i])
        ans.append("["+f[1:]+"]")
print(*ans,sep="\n")