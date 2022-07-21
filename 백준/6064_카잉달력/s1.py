import sys
sys.stdin = open('input.txt')


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())

    while x < M * N:
        if not (x-y) % N:
            print(x)
            break
        x += M
    else:
        print(-1)