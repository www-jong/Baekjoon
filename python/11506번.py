res=''
'''
while True:
    try:
        res+=input()
    except EOFError:
        break
print(res)
'''
for i in range(2):
    res+=input()
print(res)