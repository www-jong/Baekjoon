li=[int(input()) for i in range(3)]
A=(0 if li[0]<=100 else (li[0]-100)*25)+(li[1]*15)+(li[2]*20)
B=(0 if li[0]<=250 else (li[0]-250)*45)+((li[1]*35))+((li[2]*25))
print(f'Plan A costs {str(A)[:-2]}.{str(A)[len(str(A))-2:]}')
print(f'Plan B costs {str(B)[:-2]}.{str(B)[len(str(B))-2:]}')
if A==B:
    print("Plan A and B are the same price.")
elif A>B:
    print('Plan B is cheapest.')
else:
    print('Plan A is cheapest.')