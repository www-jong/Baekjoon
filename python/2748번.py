arr=[0,1]*50
for i in range(1,90):
    arr[i+1]=arr[i]+arr[i-1]
print(arr[int(input())])