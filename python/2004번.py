a,b=map(int,input().split())
def gets(num):
    two=0
    five=0
    for i in range(1,40):
        if num>=2**i:
            two+=num//2**i
        if num>=2**i:
            five+=num//5**i
    return two,five
t,f=gets(a)
t2,f2=gets(a-b)
t3,f3=gets(b)
ans=min(t-t2-t3,f-f2-f3)
print(ans)
'''
aCb=a!/b!*(a-b)!
2*5 쌍이 몇개인지 세기 

'''