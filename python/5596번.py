li=[]
li.append(list(map(int,input().split())))
li.append(list(map(int,input().split())))
print(max(sum(li[0]),sum(li[1])))