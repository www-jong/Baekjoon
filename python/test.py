first_rectangle=input()
second_rectangle=input()

A,B=[eval(tuple) for tuple in first_rectangle.split()]
C,D=[eval(tuple) for tuple in second_rectangle.split()]

if sum(A)>sum(B):
    A,B=B,A
if sum(C)>sum(D):
    C,D=D,C
if A[0]**2+A[1]**2>C[0]**2+C[1]**2:
    A,B,C,D=C,D,A,B
ax,ay=A
bx,by=B
cx,cy=C
dx,dy=D

if (cx<ax<dx and cy<ay<dy) or (cx<bx<dx and cy<by<dy) or(A==C and B==D):
    print('face')
elif bx<cx and by<cy and ax<dx and ay<dy:
    print('null')
elif (B==C) or (A==D) or (bx==cx and ay==dy) or(ax==dx and by==cy):
    print('point')
else:
    print('line')
'''
if bx<cx and ax<dx and by<cy and ay<dy:
    print('null')
elif ax==dx or ay==dy or bx==cx or by==cy:
    print('line')
elif ax==cx or bx==dx or ay==cy or by==cy:
    print('point')
else:
    print('face')
'''