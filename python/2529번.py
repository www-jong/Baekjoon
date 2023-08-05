K=int(input())
li=list(map(str,input().split()))
res=[]
all_word=[]

def check(word,lens=0):
    if len(word)==1:
        return True
    tmp=True
    if lens==0:
        for i in range(len(word)-1):
            ch=eval("True if "+word[i]+li[i]+word[i+1]+" else False")
            if not ch:
                tmp=False
                break
    else:
        tmp=eval("True if "+word[0]+li[lens-1]+word[1]+" else False")
    return tmp

all_word=[]
def func(word,p):
    global all_word
    if word!="" and len(word)==K+1:
        all_word.append(word)
        return
    for i in range(10):
        if i not in p:
            if len(word)==0:
                func(word+str(i),p+[i])
            else:
                if check(word[-1]+str(i),len(word)):
                    func(word+str(i),p+[i])

func('',[])
print(f'{all_word[-1]}\n{all_word[0]}')