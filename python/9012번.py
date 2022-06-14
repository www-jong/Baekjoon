for _ in range(int(input())):
    n=input()
    for i in range(26):
        n=n.replace("()","")
    if len(n)!=0:
        print("NO")
    else:
        print("YES")