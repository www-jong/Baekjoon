res=0
while True:
    try:
        s=input()
    except EOFError:
        break
    else:
        res+=1
print(res)