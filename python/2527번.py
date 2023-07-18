li=
for i in range(4):
    ax1,ay1,ax2,ay2,bx1,by1,bx2,by2=map(int,input().split())
    if ax1<bx1 and ay1<by1 and ax2>bx2 and ay2>by2:
        print()