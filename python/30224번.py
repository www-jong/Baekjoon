N=input()
if '7' not in N:
    if int(N)%7:
        print(0)
    else:
        print(1)
else:
    if int(N)%7:
        print(2)
    else:
        print(3)