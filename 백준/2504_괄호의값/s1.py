import sys
sys.stdin = open('input.txt')

text = input()
i = 0
stack = [text[i]]

while i < len(text)-1:
    i += 1

    # (, [의 경우 스택에 추가
    if text[i] in ['(', '[']:
        stack.append(text[i])

    # )의 경우
    elif text[i] == ')':
        tmp = 0
        while stack:
            top = stack.pop()

            if top == '(':
                if tmp == 0:
                    stack.append(2)
                else:
                    stack.append(2*tmp)
                break
            elif top == '[':
                print(0)
                sys.exit(0)
            else:
                tmp += top


    # ]의 경우
    elif text[i] == ']':
        tmp = 0

        while stack:
            top = stack.pop()

            if top == '[':
                if tmp == 0:
                    stack.append(3)
                else:
                    stack.append(3*tmp)
                break
            elif top == '(':
                print(0)
                sys.exit(0)
            else:
                tmp += top

ans = 0
for s in stack:
    if s not in ['(',')','[',']']:
        ans += s
print(ans)
