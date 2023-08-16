c = input()
answer = ''
stack = []
priority = {
    '*': 1,
    '/': 1,
    '+': -1,
    '-': -1
}
for i in '(' + c + ')':
    if i.isalpha() : # 알파벳이면 답에 추가
        answer += i
    elif i == ')': # 닫는 괄호면 열린괄호까지 스택 pop
        tmp = stack.pop()
        while tmp != '(' :
            answer += tmp
            tmp = stack.pop()
    else : # 연산자는 스택에 추가
        if i != '(' :
            while stack[-1] != '(' and priority[i] <= priority[stack[-1]]:
                answer += stack.pop()
        stack.append(i)
print(answer)