s=input()
dic={}
def func(pri,end):
    if s[pri:end] not in dic:
        dic[s[pri:end]]=1
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        func(i,j)
print(len(dic))