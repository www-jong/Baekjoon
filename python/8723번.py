li=sorted(list(map(int,input().split())))
if li[2]**2==li[1]**2+li[0]**2:
    print(1)
elif li[0]==li[1]==li[2]:
    print(2)
else:
    print(0)
