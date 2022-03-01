a=2000;b=2000
for i in range(3):
    c=int(input())
    a=a if a<c else c
for i in range(2):
    c=int(input())
    b=b if b<c else c      
print(a+b-50)