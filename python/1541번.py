a=input().replace("-","-(",1)
if '-' in a:
    a+=")"
c=eval(a)
print(c)
print(a)