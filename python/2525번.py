h,m=map(int,input().split());m+=int(input());a=h*60+m
if a>=1440:
    print("%d %d"%((a-1440)//60,(a-1440)%60))
else:
    print("%d %d"%(a//60,a%60))