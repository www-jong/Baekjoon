s=input()
check=1
for i in range(len(s)):
    if s[i]!=s[len(s)-i-1]:
        check=0
        break
print(check)