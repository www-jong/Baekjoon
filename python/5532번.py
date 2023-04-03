import math
li=[int(input()) for i in range(5)]
print(li[0]-(max((math.ceil(li[1]/li[3]),math.ceil(li[2]/li[4])))))