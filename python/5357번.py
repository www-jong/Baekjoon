for i in range(int(input())):
    S=input()
    tmp=''
    for i in S:
        if i!=tmp:
            tmp=i
            print(i,end='')
    print()
