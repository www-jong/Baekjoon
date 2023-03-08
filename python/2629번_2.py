N=int(input())
li=list(map(int,input().split()))
ball_N=int(input())
ball=list(map(int,input().split()))
dp_set=set()

for weight in li:
    tmp_set=set()
    tmp_set.add(weight)
    for i in dp_set:
        tmp_set.add(weight+i)
        tmp_set.add(abs(weight-i))
    dp_set=dp_set.union(tmp_set)
for i in ball:
    print("Y" if i in dp_set else"N",end=" ")