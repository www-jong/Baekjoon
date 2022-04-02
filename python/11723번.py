import sys
s=set()
g=[0]*21
gg=[0]*21
s_1=set(list(i for i in range(1,21)))
for i in range(int(sys.stdin.readline())):
    a=list(sys.stdin.readline().split())
    if len(a)>=2:
        num=int(a[1])
    if a[0]=="add":
        if g[num]==0:
            s.add(int(a[1]))
            g[num]=1
    elif a[0]=="remove":
        if g[num]!=0:
            s.discard(int(a[1]))
            g[num]=0
    elif a[0]=="check":
        if g[num]!=0:
             sys.stdout.write("1\n")
        else:
             sys.stdout.write("0\n")
    elif a[0]=="toggle":
        if g[num]!=0:
            s.remove(int(a[1]))
            g[num]=0
        else:
            s.add(int(a[1]))
            g[num]=1
    elif a[0]=="all":
        s=s_1.copy()
        g=[1]*21
    else:
        s.clear()
        g=[0]*21