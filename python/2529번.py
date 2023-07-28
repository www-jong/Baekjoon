K=int(input())
li=list(map(str,input().split()))
plag=False
res=[]

def check(word):
    if len(word)==1:
        return True
    tmp=True
    for i in range(len(word)-1):
        ch=exec("True if "+word[i]+li[i]+word[i+1]+" else False")
        if not ch:
            tmp=False
            break
    return tmp

def func(word,p):
    global plag,res
    if plag:
        return
    if word!="" and len(word)==K+1:
        res.append(int(word))
        plag=True
        return
    for i in range(0,10):
        if i not in p:
            stts=check(word+str(i))
            if stts:
                func(word+str(i),p+[i])

func("",[])
print(res)