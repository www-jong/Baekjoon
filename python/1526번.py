def is_good_number(num):
    while num > 0:
        digit = num % 10
        if digit != 4 and digit != 7:
            return False
        num //= 10
    return True

n = int(input())
while True:
    if is_good_number(n):
        print(n)
        break
    n -= 1
