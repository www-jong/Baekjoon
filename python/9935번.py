import sys
input=sys.stdin.readline
S=list(input().rstrip())
bomb=list(input().rstrip())
len_bomb=len(bomb)
stack=[]
idx=0
while idx!=len(S):
    stack.append(S[idx])
    if stack[-1]==bomb[-1]:
        if stack[-len_bomb:]==bomb:
            for i in range(len_bomb):
                stack.pop()
    idx+=1

print(*stack if stack else "FRULA",sep="")