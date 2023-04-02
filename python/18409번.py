dic={'a':1,'i':1,'u':1,'e':1,'o':1}
_=int(input())
s=input()
res=0
for i in s:
    if i in dic:
        res+=1
print(res)