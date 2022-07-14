n=int(input())
s = []
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])
t = sorted(s, key=lambda a: a[0])
print(t)
t = sorted(t, key=lambda a: a[1])
print(t)
print(sorted(s))
print(s)
