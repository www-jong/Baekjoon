s1,s2=0,0
for i in range(3,0,-1):
    s1+=int(input())*i
for i in range(3,0,-1):
    s2+=int(input())*i
print("A" if s1>s2 else ("B" if s2>s1 else "T"))