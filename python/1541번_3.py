a=input()
b="("
check=""
for i in a:
    if i!="+" and i!="-":
        check+=i
    else:
        if i=="+":
            b+=str(int(check))+"+"
            check=""    
        else:
            b+=str(int(check))+")-("
            check=""  
b+=str(int(check))+")"
c=eval(b)
print(c)