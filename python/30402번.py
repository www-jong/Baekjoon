li=[]
for i in range(15):
    li.extend(input().split())
r=''
for i in li:
    if i in 'royp':
        continue
    if i=='w':
        r='chunbae'
        break
    elif i=='b':
        r='nabi'
        break
    elif i=='g':
        r='yeongcheol'
        break
print(r)
