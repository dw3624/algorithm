import sys
sys.stdin = open('input.txt')


import sys
from collections import deque


T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    register = [0] * 10000
    register[A] = 1
    q = deque([(A, '')])

    while q:
        n, commands = q.popleft()

        if n == B:
            print(commands)
            break

        nn = (n * 2) % 10000
        if not register[nn]:
            register[nn] = 1
            q.append((nn, commands + 'D'))

        nn = (n - 1) % 10000
        if not register[nn]:
            register[nn] = 1
            q.append((nn, commands + 'S'))

        nn = ((n * 10) % 10000) + n // 1000
        if not register[nn]:
            register[nn] = 1
            q.append((nn, commands + 'L'))

        nn = ((n % 10) * 1000) + n // 10
        if not register[nn]:
            register[nn] = 1
            q.append((nn, commands + 'R'))