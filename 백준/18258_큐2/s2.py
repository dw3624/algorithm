import sys
sys.stdin = open('input.txt')


from collections import deque
import sys


input = sys.stdin.readline
n = int(input())
q = deque([])
def commands():
    query = input().split()
    if len(query) > 1:
        return q.append(int(query[1]))
    else:
        c = query[0]

    if c == 'pop':
        return print(q.popleft()) if q else print(-1)
    if c == 'front':
        return print(q[0]) if q else print(-1)
    if c == 'back':
        return print(q[-1]) if q else print(-1)
    if c == 'size':
        return print(len(q))
    if c == 'empty':
        return print(0) if q else print(1)


for _ in range(n):
    commands()