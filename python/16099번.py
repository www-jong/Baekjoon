for i in range(int(input())):
    l,w,le,we=map(int,input().split())
    if l*w==le*we:
        print('Tie')
    elif l*w>le*we:
        print('TelecomParisTech')
    else:
        print('Eurecom')
