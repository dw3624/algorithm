import sys
# sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

stack = []
for _ in range(N):
    commands = sys.stdin.readline().split()
    command = commands[0]

    if command == 'push':
        stack += [commands[1]]

    elif command == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif command == 'size':
        print(len(stack))

    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif command == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])