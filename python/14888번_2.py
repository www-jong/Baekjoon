#너무 느림
arr=[]
INF=1000000000
maxv=-INF
minv=INF
def func():

    def ffun():
        global maxv
        global minv
        vv=nums[0]
        if len(arr)==n-1:
            for i in range(n-1):
                comp='vv'+arr[i]+str(nums[i+1])
                vv=int(eval(comp))
            if vv>maxv:maxv=vv
            if vv<minv:minv=vv
            return
        for i in range(n-1):
            if sepa[i]!='x':
                arr.append(sepa[i])
                ww=sepa[i]
                sepa[i]='x'
                ffun()
                arr.pop()
                sepa[i]=ww
    ffun()
    return
arr=[]
n=int(input())
nums=list(map(int,input().split()))
sepas=list(map(int,input().split()))
sepa=['+']*sepas[0]+['-']*sepas[1]+['*']*sepas[2]+['/']*sepas[3]
func()
print(maxv)
print(minv)
    
    

    