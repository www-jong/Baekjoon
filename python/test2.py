n=int(input())
def bitcount(n):
    if n==0:
        return 0
    return n%2+bitcount(n//2)

print(bitcount(n),bin(n))

b=n
b&=~1<<3
print(b, bin(b))
print(len(bin(b)))