for i in range(int(input())):
    a=0
    for i in range(9):
        n,m=map(int,input().split())
        a+=n
        a-=m
    print("Yonsei" if a>0 else ("Korea" if a<0 else "Draw"))