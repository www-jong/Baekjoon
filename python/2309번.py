d=[]
for i in range(9):
    d.append(int(input()))
d.sort()
list=[]
count=0
def func():
    global count
    if count==1:
        return
    if len(list)==7:
        if sum(list)==100:
            print(*list,sep="\n")
            count+=1
            return
        return
    for i in d:
        if i not in list:
            list.append(i)
            func()
            list.pop()
func()        