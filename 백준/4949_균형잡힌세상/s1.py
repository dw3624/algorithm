import sys
sys.stdin = open('input.txt')
# 백준에서는 readlines() 사용불가


while True:
    text = input()

    if text == '.':
        break

    stack = []
    for t in text:
        if (t == '[') | (t == '('):
            stack.append(t)
        elif t == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif t == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(']')
                break
        elif t == '.':
            break

    if stack:
        print('no')
    else:
        print('yes')