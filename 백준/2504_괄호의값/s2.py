import sys
sys.stdin = open('input.txt')

text = input()
stack = []

for t in text:
    if t == ')':
        tmp = 0

        if not stack:
            print(0)
            sys.exit(0)

        while stack:
            top = stack.pop()

            if top == '[':
                print(0)
                sys.exit(0)
            elif top == '(':
                if tmp == 0:
                    stack.append(2)
                else:
                    stack.append(2*tmp)
                break
            else:
                tmp += top

    elif t == ']':
        tmp = 0
        if not stack:
            print(0)
            sys.exit(0)

        while stack:
            top = stack.pop()

            if top == '(':
                print(0)
                sys.exit(0)
            elif top == '[':
                if tmp == 0:
                    stack.append(3)
                else:
                    stack.append(3*tmp)
                break
            else:
                tmp += top

    elif t in ['(', '[']:
        stack.append(t)

    else:
        print(0)
        sys.exit(0)

    # print(stack)

ans = 0
for s in stack:
    if s in ['(', '[']:
        print(0)
        sys.exit(0)
    else:
        ans += s
print(ans)