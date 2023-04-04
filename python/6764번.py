li=[int(input()) for i in range(4)]
if li[0]==li[1]==li[2]==li[3]:
    print('Fish At Constant Depth')
elif li[0]<li[1]<li[2]<li[3]:
    print('Fish Rising')
elif li[0]>li[1]>li[2]>li[3]:
    print('Fish Diving')
else:
    print('No Fish')