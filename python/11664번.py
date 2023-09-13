def f(x, y):
    return abs(x - y) ** 2

ax, ay, az, bx, by, bz, cx, cy, cz = map(int, input().split())

a_b = (f(ax, bx) + f(ay, by) + f(az, bz))**0.5
a_c = (f(ax, cx) + f(ay, cy) + f(az, cz))**0.5
b_c = (f(bx, cx) + f(by, cy) + f(bz, cz))**0.5

A = [bx - ax, by - ay, bz - az]
B = [cx - ax, cy - ay, cz - az]

S = abs(A[0] * B[1] - A[1] * B[0]) ** 2 + abs(A[1] * B[2] - A[2] * B[1]) ** 2 + abs(A[2] * B[0] - A[0] * B[2]) ** 2
S = S ** 0.5 / 2
if not a_b:
    print(a_c)
else:
    if S:
        res=(S*2)/a_b
        if a_c**2>res**2+a_b**2 or b_c**2>res**2+a_b**2:
            print(min(a_c,b_c))
        else:
            print(res)
    else:
        if (ax<=cx<=bx or ax>=cx>=bx)and(ay<=cy<=by or ay>=cy>=by)and(az<=cz<=bz or az>=cz>=bz):
            print(0)
        else:
            print(min(a_c,b_c))