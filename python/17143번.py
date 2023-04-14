R,C,M=map(int,input().split())
# R:세로, C: 가로
li=[[0]*(C) for i in range(R)]
sharks={}
res=0
UP,DOWN,RIGHT,LEFT=1,2,3,4
for i in range(1,M+1):
    r,c,s,d,z=map(int,input().split())
    # r,c: 상어위치 li[r][c]
    # s: 속력, d: 이동방향, z: 크기
    li[r-1][c-1]=i
    sharks[i]=[r-1,c-1,s,d,z]
def shark_move():
    global sharks
    for i in sharks.copy().keys():
        r,c,s,d,z=sharks[i]
        new_r,new_c,new_d=get_next_loc(r,c,s,d)
        if li[new_r][new_c]==0:
            sharks[i]=[new_r,new_c,s,new_d,z]
            li[r][c]=0
            li[new_r][new_c]=i
        else:
            if li[new_r][new_c]==i:
                sharks[i]=[new_r,new_c,s,new_d,z]
            elif li[new_r][new_c] in sharks:
                if sharks[li[new_r][new_c]][4]<z:
                    del sharks[li[new_r][new_c]]
                    li[new_r][new_c]=i
                    li[r][c]=0
                    sharks[i]=[new_r,new_c,s,new_d,z]
                else:
                    del sharks[i]
                    li[r][c]=0
            else:
                li[new_r][new_c]=i
                li[r][c]=0
                sharks[i]=[new_r,new_c,s,new_d,z]
def get_next_loc(i, j, speed, dir):

    if dir == UP or dir == DOWN:  # i
        cycle = R * 2 - 2
        if dir == UP:
            speed += 2 * (R - 1) - i
        else:
            speed += i

        speed %= cycle
        if speed >= R:
            return (2 * R - 2 - speed, j, UP)
        return (speed, j, DOWN)

    else:  # j
        cycle = C * 2 - 2
        if dir == LEFT:
            speed += 2 * (C - 1) - j
        else:
            speed += j

        speed %= cycle
        if speed >= C:
            return (i, 2 * C - 2 - speed, LEFT)
        return (i, speed, RIGHT)

for i in range(C):
    for j in range(R):
        if li[j][i]!=0:
            res+=sharks[li[j][i]][4]
            del sharks[li[j][i]]
            li[j][i]=0
            break
    shark_move()
print(res)