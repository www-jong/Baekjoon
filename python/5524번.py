for _ in range(int(input())):
    S=input()
    for i in S:
        print(i if ord(i)>90 else str(chr(ord(i)+32)),end='')
    print()