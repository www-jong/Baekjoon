res=0
for i in range(int(input())):
    S=input()
    if int(S[2:])<=90:
        res+=1
print(res)