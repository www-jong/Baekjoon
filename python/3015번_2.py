import sys
input=sys.stdin.readline
N=int(input())
li=[int(input()) for _ in range(N)]
stk=[]
res=0
dic={}
high=0
def dict_ctl(val,type=0):
    global dic
    if type:
        if val not in dic:
            dic[val]=1
        else:
            dic[val]+=1
    else:
        if val in dic:
            del dic[val]

for i in range(N):
    print(f'start:{li[i]} , ',end='')
    high=max(high,li[i])
    if not stk:
        stk.append((li[i],i))
        dict_ctl(li[i],1)
        continue

    print(f'{stk}')
    if li[i]<stk[-1][0]: # 더 작은키가 들어올때,
        #stk.append((li[i],i))
        res+=1
        print(f'stk:{stk}, res={res}, now={li[i]}')
    elif li[i]==stk[-1][0]:
        if stk:
            if high==li[i]:
                res+=dic[li[i]]
            else:
                res+=dic[li[i]]+1
                print(f'stk:{stk}, res={res}, now={li[i]}')
    else: # 더 큰키가 들어올 때,
        while stk:
            if stk[-1][0]<li[i]:
                dict_ctl(stk[-1][0],0)
                stk.pop()
                res+=1
                print(f'stk:{stk}, res={res}, now={li[i]}')
            elif stk[-1][0]==li[i]:
                if high==li[i]:
                    res+=dic[li[i]]
                else:
                    res+=dic[li[i]]+1
                print(f'stk:{stk}, res={res}, now={li[i]} , same')
                break
            else:
                res+=1
                print(f'stk:{stk}, res={res}, now={li[i]}')
                break

    dict_ctl(li[i],1)
    stk.append((li[i],i))
print(res)
'''
14
7
7
8
6
5
3
7
4
7
7
10
6
1
2

10
10
9
1
3
8
6
7
8
5
8

'''