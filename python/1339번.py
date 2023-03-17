N=int(input())
words=[[0,chr(i+65)] for i in range(10)]
idx=9
res=0
for i in range(N):
    S=input()[::-1]
    for i in range(len(S)):
        words[ord(S[i])-65][0]+=10**(i)
words.sort(key=lambda x:x[0],reverse=True)
while True:
    if words[idx][0]==0:
        words.pop()
        idx-=1
    else:break
for i in range(len(words)):
    res+=words[i][0]*(9-i)
print(res)