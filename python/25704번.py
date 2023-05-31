N=int(input())
P=int(input())
if N>=5:
    if N<10:
        print(P-500 if P-500>0 else 0)
    elif N<15:
        print(min(int(P*0.9),P-500)if min(int(P*0.9),P-500)>0 else 0)
    elif N<20:
        print(min(int(P*0.9),P-2000) if min(int(P*0.9),P-2000)>0 else 0)
    elif N>=20:
        print(min(int(P*0.75),P-2000)if min(int(P*0.75),P-2000)>0 else 0)
else:
    print(P)