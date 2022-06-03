while True:
    a,b=map(int,input().split())
    if a==b and a==0:break
    else:
        print("Yes" if a>b else "No")