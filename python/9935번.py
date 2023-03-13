S=input()
bomb=input()
while True:
    tmp_S=S.replace(bomb,'')
    if S==tmp_S:
        S=tmp_S
        break
    S=tmp_S
print('FRULA' if len(S)==0 else S)