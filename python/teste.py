import heapq,random
while True:
    a=[]
    ans=int(input())
    if ans==0:
        break
    b=[i for i in range(1,ans+1)]
    random.shuffle(b)
    for i in b:
        heapq.heappush(a,i)
    print(a)
    print('중간값 위치:  %d:%d'%(ans//2+ans%2,a.index(ans//2+ans%2)))
