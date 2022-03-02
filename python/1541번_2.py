a=input()
b="("
check=0
for i in a:
    if i=="-":
        b+=")-("
    else:
        b+=i
b+=")"
c=eval(b)
print(c)
print(b)