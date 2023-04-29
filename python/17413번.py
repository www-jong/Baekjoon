S=input()
stk=[]
check=0
res=''
def stk_pop():
    global res
    while stk:
        res+=stk.pop()

for i in S:
    if check:
        if i=='>':
            check=0
        res+=i
    else:
        if i=='<':
            stk_pop()
            res+=i
            check=1
        else:
            if i==' ':
                stk_pop()
                res+=i
            else:
                stk.append(i)
stk_pop()
print(res)