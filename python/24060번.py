N,K=map(int,input().split())
li=list(map(int,input().split()))

ans=[]
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = (len(arr)+1)//2
   
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    i,j = 0,0
    tmp = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            tmp.append(left[i])
            ans.append(left[i])
            i+=1
        else:
            tmp.append(right[j])
            ans.append(right[j])
            j+=1
    while i < len(left):
        tmp.append(left[i])
        ans.append(left[i])
        i+=1
    while j < len(right):
        tmp.append(right[j])
        ans.append(right[j])
        j+=1
    
    return tmp
merge_sort(li)
print(ans[K-1] if len(ans)>K else -1)