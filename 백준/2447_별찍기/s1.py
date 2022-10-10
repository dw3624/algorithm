import sys
sys.stdin = open('input.txt')


def star(sr, sc, n):
    if n == 1:
        return

    for r in range(sr + n // 3, sr + 2 * n // 3):
        for c in range(sc + n // 3, sc + 2 * n // 3):
            res[r][c] = ' '

    for r in range(sr, sr + n, n//3):
        for c in range(sc, sc + n, n//3):
            if n // 3 <= r < 2 * n // 3 and n // 3 <= c < 2 * n // 3:
                continue
            star(r, c, n//3)


n = int(input())
res = [['*'] * n for _ in range(n)]
star(0, 0, n)
[print(''.join(r)) for r in res]