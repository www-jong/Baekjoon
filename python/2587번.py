li=[]
for i in range(5):
    li.append(int(input()))
li.sort()
print(sum(li)/5)
print(li[2])