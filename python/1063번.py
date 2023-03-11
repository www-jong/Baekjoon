maps=[[0]*(9) for i in range(9)]

    

def trans(x,type=0):
    if type==0:
        return ord(x)-64
    else:
        if x=='R':
            d=[0,1]
        elif x=='L':
            d=[0,-1]
        elif x=='B':
            d=[1,0]
        elif x=='T':
            d=[-1,0]
        elif x=='RT':
            d=[-1,1]
        elif x=='LT':
            d=[-1,-1]
        elif x=='RB':
            d=[1,1]
        elif x=='LB':
            d=[-1,-1]
        return d

def check(d):
    global king,phone
    dking=[king[0]+d[0],king[1]+d[1]]
    if dking==phone:
        if (phone[0]+d[0]>=1 and phone[0]+d[0]<=8) and (phone[1]+d[1]>=1 and phone[1]+d[1]<=8):
            king=[king[0]+d[0],king[1]+d[1]]
            phone=[phone[0]+d[0],phone[1]+d[1]]
    else:
        if (king[0]+d[0]>=1 and king[0]+d[0]<=8) and (king[1]+d[1]>=1 and king[1]+d[1]<=8):
            king=[king[0]+d[0],king[1]+d[1]]
king,phone,N=map(str,input().split())
king=[trans(king[0]),int(king[1])]
phone=[trans(phone[0]),int(phone[1])]
print(f'{king} : {phone} ')
for _ in range(int(N)):
    d=trans(input(),1)
    check(d)
    print(f'{king} : {phone} , {_+1}')
print(trans('A'))
print(king)
print(phone)