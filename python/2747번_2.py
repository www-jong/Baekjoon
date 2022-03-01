arr=[0,1]*25
for i in range(1,45):
    arr[i+1]=arr[i]+arr[i-1]
print(arr[int(input())])