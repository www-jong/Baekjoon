a=0
for _ in range(5):
    c=int(input())
    a+=c if c>=40 else 40
print(int(a/5))