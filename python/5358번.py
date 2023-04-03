dic={'i':'e','e':'i','I':'E','E':'I'}
while True:
    try:
        s=input()
    except EOFError:
        break
    else:
        for i in s:
            if i in dic:
                print(dic[i],end='')
            else:
                print(i,end='')
        print()