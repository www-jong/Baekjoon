a=[]
for i in range(int(input())):
    s=int(input())
    if s==0:
        a.pop()
    else:
        a.append(s)
print(sum(a))