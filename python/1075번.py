n=input()
f=int(input())
for i in range(100):
    if int(n[0:len(n)-2]+str(i if i>10 else "0"+str(i)))%f==0:
        print(int(i) if i>10 else int("0"+str(i)))
        break
    