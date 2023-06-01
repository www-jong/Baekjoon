ali=[0]+[500]+[300]*2+[200]*3+[50]*4+[30]*5+[10]*6
bli=[0]+[512]+[256]*2+[128]*4+[64]*8+[32]*16
for i in range(int(input())):
    res=0
    a,b=map(int,input().split())
    if a<=21:
        res+=ali[a]
    if b<=31:
        res+=bli[b]
    print(res*10000)