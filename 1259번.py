while True:
    c=input()
    if c=="0":
        break
    for i in range(len(c)//2):
        if c[i]!=c[len(c)-1-i]:
            print("no")
        else:
            print("yes")