n=int(input())
print('int a;')
print('int *ptr = &a;')
for i in range(2,n+1):
    a='*'*i
    if i-1!=1:
        print(f'int {a}ptr{i} = &ptr{i-1};')
    else:
        print(f'int {a}ptr{i} = &ptr;')