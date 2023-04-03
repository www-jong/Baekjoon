dic={'a','e','i','o','u','A','E','I','O','U'}
while True:
    S=input()
    res=0
    if S=='#':
        break
    for i in S:
        if i in dic:
            res+=1
    print(res)
    