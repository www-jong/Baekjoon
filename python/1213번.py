S=input()
word={}
for i in S:
    if i not in word:
        word[i]=1
    else:
        word[i]+=1
check=0
for i in word.values():
    if i%2!=0:
        check+=1
if not check or (len(S)%2!=0 and check==1):
    if not check:
        words=[]
        for k,v in word.items():
            for i in range(v//2):
                words.append(k)
        res=''.join(sorted(words))
        print(res+res[::-1])
    else:
        medium=''
        words=[]
        for k,v in word.items():
            if v%2!=0:
                medium=k
            for i in range(v//2):
                words.append(k)
        res=''.join(sorted(words))
        print(res+medium+res[::-1])
else:
    print("I'm Sorry Hansoo")