S="("+input()+")"
stk=[]
res=''
prio={'*':1,'/':1,'+':-1,'-':-1}
for i in S:
    if i.isalpha():
        res+=i
    else:
        if stk:
            if i==")":
                while stk[-1]!="(":
                    res+=stk.pop()
                stk.pop()
            else:
                if i!="(":
                    while stk and stk[-1]!="(" and prio[i]<=prio[stk[-1]]:
                        res+=stk.pop()
                stk.append(i)
        else:
            stk.append(i)
print(res)