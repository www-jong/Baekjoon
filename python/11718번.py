c="d"
while c:
    try:
        c=input()
        print(c)
    except EOFError:
        break