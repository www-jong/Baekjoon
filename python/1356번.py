S=input()
res="NO"
for i in range(1,len(S)):
    f,b=1,1
    for j in S[:i]:
        f*=int(j)
    for j in S[i:]:
        b*=int(j)
    if f==b:
        res="YES"
        break
print(res)