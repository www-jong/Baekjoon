N=int(input())
li=[]
last=[]
for i in range(N):
    S=input()
    if 'boj.kr/' in S:
        last.append(int(S[7:]))
    else:
        li.append(S)
li.sort(key=lambda x:[len(x),x])
last.sort()
for i in li:
    print(i)
for i in last:
    print('boj.kr/'+str(i))
