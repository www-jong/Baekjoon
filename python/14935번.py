x=int(input())
res,ch=x,0
for i in range(200):
    tres=len(str(res))*int(str(res)[0])
    if tres==res:
        print('FA')
        ch=1
        break
    res=tres
if ch==0:
    print('NFA')