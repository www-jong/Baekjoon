S=input()
for i in S:print(chr(ord(i)+(-32 if ord(i)>96 else+32)),end="")
