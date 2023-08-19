N=int(input())
li=list(map(int,input().split()))
for i in li:
    idx=0
    if 300<=i:
        idx=1
    elif 275<=i:
        idx=2
    elif 250<=i:
        idx=3
    else:
        idx=4
    print(idx,end=" ")
