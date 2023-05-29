T=int(input())
for i in range(T):
    s=input()
    res=0
    for i in range(26):
        if len(s)>i:
            if ord(s[i])!=i+65:
                res+=i+65
        else:
            res+=i+65
    print(res)