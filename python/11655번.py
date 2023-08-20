S=list(input())
t=[]
for i in S:
    if i.isalpha():
        if 65<=ord(i)<=90:
            t.append(chr((ord(i)-52)%26+65))
        else:
            t.append(chr((ord(i)-84)%26+97))
    else:
        t.append(i)
print(*t,sep="")