import sys
import heapq as hq
input=sys.stdin.readline

for m in range(int(input())):
    res=0
    min_hp=[]
    min_set=set()
    max_hp=[]
    max_set=set()
    plag=0
    for i in range(int(input())):
        a,b=input().split()
        b=int(b)
        #print(f'{min_hp} {max_hp} {a}:{b}')
        if a=='I':
            if not plag:plag=1
            hq.heappush(min_hp,b)
            hq.heappush(max_hp,(-b,b))
        else:
            if plag:
                if min_hp[0]<max_hp[0][1]:
                    if b==1:
                        hq.heappop(max_hp)
                    else:
                        hq.heappop(min_hp)
                elif min_hp[0]==max_hp[0][1]:
                    hq.heappop(max_hp)
                    hq.heappop(min_hp)
                if len(min_hp) == 0 or len(max_hp) == 0 or min_hp[0] > max_hp[0][1]:
                    plag = 0
                    min_hp = []
                    max_hp = []
                    continue

    print(str(max_hp[0][1])+' '+str(min_hp[0]) if plag else 'EMPTY')
'''
D 1: q에서 최대값 삭제(1개만)
D -1: q에서 최소값 삭제(1개만)

L n : q에 n 삽입
1

9

I 36

I 37

I 38

D 1

D 1

I 39

I 40

D -1

D -1

answer  : 40 40

'''