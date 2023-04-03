while True:
    li=list(map(str,input().split()))
    if li[0]=='#':
        break
    if int(li[1])>17 or int(li[2])>=80:
        print(f'{li[0]} Senior')
    else:
        print(f'{li[0]} Junior')