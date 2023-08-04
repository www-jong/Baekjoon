
def gap(x, y, z=None):
    if z is None:
        r = sum([1 for g in range(4) if x[g] != y[g]])
    else:
        r = sum([1 for g in range(4) if x[g] != y[g]])
        r += sum([1 for g in range(4) if x[g] != z[g]])
        r += sum([1 for g in range(4) if y[g] != z[g]])
    return r


for _ in range(int(input())):
    N = int(input())
    li = list(map(str, input().split()))
    if N>32:
        print(0)
        continue
    dic,res = {}, 10**10
    check=0
    for i in li:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
            if dic[i]==3:
                check=1
                break
    if check:
        print(0)

        continue
    li = list(set(li))
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            for k in range(j + 1, len(li)):
                if dic[li[i]] >= 2:
                    res = min(res, gap(li[i], li[j]) * 2,gap(li[i], li[k]) * 2)
                if dic[li[j]] >= 2:
                    res = min(res, gap(li[j], li[i]) * 2,gap(li[j], li[k]) * 2)
                if dic[li[k]] >= 2:
                    res = min(res, gap(li[k], li[i]) * 2,gap(li[k], li[j]) * 2)
                res = min(res, gap(li[i], li[j], li[k]))
    if len(li)<=2:
        res=min(res,gap(li[0],li[1])*2)
    print(res)