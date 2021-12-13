# import sys
# sys.stdin = open('input.txt')

from sys import stdin

N = int(stdin.readline())
que = []

for _ in range(N):
    cmd = stdin.readline()

    if 'push' in cmd:
        tmp = cmd.split()[1]
        que.append(tmp)

    elif 'pop' in cmd:
        print(que.pop(0)) if que else print(-1)

    elif 'size' in cmd:
        print(len(que))

    elif 'empty' in cmd:
        print(1) if not que else print(0)

    elif 'front' in cmd:
        print(que[0]) if que else print(-1)

    else:
        print(que[-1]) if que else print(-1)

