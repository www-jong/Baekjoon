r = 0

t = int(input())
sub = list(map(int, input().split())) + [0] * (5 - t)
if sub[0] > sub[2]:
    r += (sub[0] - sub[2]) * 508
else:
    r += (sub[2] - sub[0]) * 108
if sub[1] > sub[3]:
    r += (sub[1] - sub[3]) * 212
else:
    r += (sub[3] - sub[1]) * 305
if sub[4] > 0:
    r += sub[4] * 707
r *= 4763
print(r)