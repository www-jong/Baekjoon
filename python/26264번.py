N=int(input())
S=input()
a,b=S.count('security'),S.count('bigdata')
if a>b:
    print("security!")
elif a<b:
    print("bigdata?")
else:
    print("bigdata? security!")