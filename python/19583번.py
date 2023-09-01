import sys
input=sys.stdin.readline
S,E,Q=input().split()
S=int(S.replace(":",""))
E=int(E.replace(":",""))
Q=int(Q.replace(":",""))
li=[]
while True:
    try:
        time,name=input().split()
        time=int(time.replace(":",""))
        li.append([time,name])
    except:
        break
dic={}
check=set()
res=0
for time,name in li:
    if time<=S and name not in dic:
        dic[name]=1
    elif E<=time<=Q and name in dic and name not in check:
        res+=1
        check.add(name)
print(res)