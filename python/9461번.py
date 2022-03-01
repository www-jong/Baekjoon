p=[0,1,1,1,2,2,3,4,5,7,9]*11
for i in range(10,101):
    p[i+1]=p[i]+p[i-4]
for i in range(int(input())):
    print(p[int(input())])    