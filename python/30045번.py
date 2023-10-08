r=0
for i in range(int(input())):
    s=input()
    if '01' in s or 'OI' in s:
        r+=1
print(r)