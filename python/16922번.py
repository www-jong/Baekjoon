import sys
sys.setrecursionlimit(10**6)
N = int(input())
nums = [1,5,10,50]
ans_list = []
sum_set = set()
def dfs(depth,N,idx):

    if depth == N:
        sum_set.add(sum(ans_list))
        return

    for i in range(idx,4):
        ans_list.append(nums[i])
        dfs(depth+1,N,i)
        ans_list.pop()

dfs(0,N,0)

print(len(sum_set))