N=int(input())
r=[
'Never gonna give you up',
'Never gonna let you down',
'Never gonna run around and desert you',
'Never gonna make you cry',
'Never gonna say goodbye',
'Never gonna tell a lie and hurt you',
'Never gonna stop'
]
g='No'
for i in range(N):
    S=input()
    if S not in r:
        g='Yes'
print(g)