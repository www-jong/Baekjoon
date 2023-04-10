s=input()
if len(s)==2:
    print(int(s[0])+int(s[1]))
elif len(s)==3:
    if s[1]=='0':
        print(int(s[0]+s[1])+int(s[2]))
    else:
        print(int(s[0])+int(s[1]+s[2]))
else:
    print(int(s[0]+s[1])+int(s[2]+s[3]))