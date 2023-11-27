ac,ad=map(int,input().split())
bc,bd=map(int,input().split())
while True:
    ad-=bc
    bd-=ac
    if ad<=0 and bd<=0:
        print('DRAW')
        break
    elif ad<=0:
        print('PLAYER B')
        break
    elif bd<=0:
        print('PLAYER A')
        break