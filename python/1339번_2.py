N=int(input())
words_dic={}
words=[]
idx=9
res=0
for i in range(N):
    S=input()[::-1]
    for i in range(len(S)):
        if S[i] in words_dic:
            words_dic[S[i]]+=10**(i)
        else:
            words_dic[S[i]]=10**(i)
for k,v in words_dic.items():
    words.append(v)
words.sort(reverse=True)
for i in range(len(words)):
    res+=words[i]*(9-i)
print(res)