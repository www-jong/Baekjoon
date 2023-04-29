first=100
for i in range(1,101):
    tmp=first
    co=i
    day=1
    while first*2>tmp:
        tmp*=(1+i*0.01)
        day+=1
    print(f'{i} : {day}')