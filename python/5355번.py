for i in range(int(input())):
    li=list(input().split())
    ans=float(li[0])
    for i in li:
        if i==li[0]:continue
        elif i=="@":
            ans*=3
        elif i=="%":
            ans+=5
        else:
            ans-=7
    print("%.2f"%(ans))