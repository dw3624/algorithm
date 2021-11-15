import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    bar = list(input())
    stack = []

    while bar:
        v = bar.pop(0)

        if v == '(':
            stack.append(v)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(v)
                break

    if stack:
        print('NO')
    else:
        print('YES')