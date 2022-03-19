c=input()
for i in range(len(c)//10+1):
    print(c[i*10:i*10+10 if i+10<len(c) else len(c)])