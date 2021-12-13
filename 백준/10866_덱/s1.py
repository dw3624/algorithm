import sys
sys.stdin = open('input.txt')


from sys import stdin
from collections import deque

N = int(stdin.readline())
que = deque()

for _ in range(N):
    cmd = stdin.readline()

    if 'push_front' in cmd:
        tmp = cmd.split()[1]
        que.appendleft(tmp)

    elif 'push_back' in cmd:
        tmp = cmd.split()[1]
        que.append(tmp)

    elif 'pop_front' in cmd:
        print(que.popleft()) if que else print(-1)

    elif 'pop_back' in cmd:
        print(que.pop()) if que else print(-1)

    elif 'size' in cmd:
        print(len(que))

    elif 'empty' in cmd:
        print(1) if not que else print(0)

    elif 'front' in cmd:
        print(que[0]) if que else print(-1)

    else:
        print(que[-1]) if que else print(-1)