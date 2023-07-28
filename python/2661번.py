import sys
sys.setrecursionlimit(1000000)
N,res=int(input()),[]
plag=False
def check(tmp):
    res=True
    for i in range(1,1+(len(tmp)+2)//2):
        if tmp[len(tmp)-i:len(tmp)]==tmp[len(tmp)-i*2:len(tmp)-i]:
            res=False
            break
    return res

def func(word):
    global res,plag
    if plag:
        return
    if len(word)==N:
        res.append(int(word))
        plag=True
        return True
    for i in range(1,4):
        if word!="" and i==word[-1]:continue
        if check(word+str(i)):
            if func(word+str(i)):
                break
            #break
func("")
print(min(res))