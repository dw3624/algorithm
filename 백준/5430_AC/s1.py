import sys
sys.stdin = open('input.txt')


from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    x = input()[1:-1].split(',')

    xs = deque(x)
    if n == 0:
        xs = deque()

    rev = 0
    for i in p:
        if i == 'R':
            rev += 1
        elif i == 'D':
            if len(xs) == 0:
                print('error')
                break
            else:
                if rev % 2:
                    xs.pop()
                else:
                    xs.popleft()

    else:
        if rev % 2:
            xs.reverse()
        print('['+','.join(xs)+']')