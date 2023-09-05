li = [list(map(int, input().split())) for _ in range(3)]
total_num = 0

if li[0][0] == 0 and li[1][1] == 0 and li[2][2] == 0:
    num1 = li[0][1] + li[0][2]
    num2 = li[1][0] + li[1][2]
    num3 = li[2][1] + li[2][0]
    diff_num = (num1-num2) + (num1-num3)
    num1 = num1 - diff_num
    num1 = num1//2
    total_num = num1 + li[0][1] + li[0][2]
elif li[0][2] == 0 and li[1][1] == 0 and li[2][0] == 0:
    num1 = li[0][0] + li[0][1]
    num2 = li[1][0] + li[1][2]
    num3 = li[2][1] + li[2][2]
    diff_num = (num1-num2) + (num1-num3)
    num1 = num1 - diff_num
    num1 = num1//2
    total_num = num1 + li[0][0] + li[0][1]

elif li[0][0] != 0 and li[1][1] != 0 and li[2][2] != 0:
    total_num = li[0][0] + li[1][1] + li[2][2]
elif li[0][2] != 0 and li[1][1] != 0 and li[2][0] != 0:
    total_num = li[0][2] + li[1][1] + li[2][0]
else:
    for i in range(3):
        if li[i][0] != 0 and li[i][1] != 0 and li[i][2] != 0:
            total_num = li[i][0] + li[i][1] + li[i][2]
            break
    if total_num == 0:
        # 세로 값 확인하기
        for i in range(3):
            if li[0][i] != 0 and li[1][i] != 0 and li[2][i] != 0:
                total_num = li[0][i] + li[1][i] + li[2][i]
                break

for i in range(3):
    for j in range(3):
        if li[i][j] == 0:
            total1 = 0
            
            if j == 0 and li[i][1] != 0 and li[i][2] != 0:
                total1 = li[i][1] + li[i][2]
            elif j == 1 and li[i][0] != 0 and li[i][2] != 0:
                total1 = li[i][0] + li[i][2]
            elif j == 2 and li[i][0] != 0 and li[i][1] != 0:
                total1 = li[i][0] + li[i][1]

            elif i == 0 and li[1][j] != 0 and li[2][j] != 0:
                total1 = li[1][j] + li[2][j]
            elif i == 1 and li[0][j] != 0 and li[2][j] != 0:
                total1 = li[0][j] + li[2][j]
            elif i == 2 and li[0][j] != 0 and li[1][j] != 0:
                total1 = li[0][j] + li[1][j]

            elif i == 0 and j == 0 and li[1][1] != 0 and li[2][2] != 0:
                total1 = li[1][1] + li[2][2]
            elif i == 1 and j == 1 and li[0][0] != 0 and li[2][2] != 0:
                total1 = li[0][0] + li[2][2]
            elif i == 2 and j == 2 and li[1][1] != 0 and li[0][0] != 0:
                total1 = li[1][1] + li[0][0]
                
            elif i == 0 and j == 2 and li[1][1] != 0 and li[2][0] != 0:
                total1 = li[1][1] + li[2][0]
            elif i == 1 and j == 1 and li[0][2] != 0 and li[2][0] != 0:
                total1 = li[0][2] + li[2][0]
            elif i == 2 and j == 0 and li[1][1] != 0 and li[0][2] != 0:
                total1 = li[1][1] + li[0][2]

            print(total_num-total1, end=' ')
        else:
            print(li[i][j], end=' ')
    print()