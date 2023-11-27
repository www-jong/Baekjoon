bx,by=map(int,input().split())
dx,dy=map(int,input().split())
jx,jy=map(int,input().split())
J=abs(dx-jx)+abs(dy-jy)
B=max(abs(bx-jx),abs(by-jy))
if B<J:
    print('bessie')
elif B>J:
    print('daisy')
else:
    print('tie')