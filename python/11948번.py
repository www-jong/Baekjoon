li=[int(input()) for _ in range(6)]
print(sum(sorted(li[:4])[1:])+max(li[4],li[5]))