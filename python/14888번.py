# 연산자의 우선순위가 무시되는거를 고려안함 .

arr=[]
INF=1000000000
maxv=-INF
minv=INF
def func():

    def ffun():
        global maxv
        global minv
        val=''
        vv=0
        if len(arr)==n-1:
            for i in range(n-1):
                val+=str(nums[i])+arr[i]
            val+=str(nums[n-1])
            print(val)
            vv=int(eval(val))
            if vv>maxv:maxv=vv
            if vv<minv:minv=vv
            return
        for i in range(n-1):
            if sepa[i]!='x':
                arr.append(sepa[i])
                ww=sepa[i]
                sepa[i]='x'
                func()
                arr.pop()
                sepa[i]=ww
    ffun()

    return


count=0
arr=[]
n=int(input())
nums=list(map(int,input().split()))
sepas=list(map(int,input().split()))
sepa=['+']*sepas[0]+['-']*sepas[1]+['*']*sepas[2]+['%']*sepas[3]
func()
print(maxv)
print(minv)
    
    

    