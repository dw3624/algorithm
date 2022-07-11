import sys
sys.stdin = open('input.txt')


M, N = map(int, input().split())
honeycomb = [[1]*M for _ in range(M)]
growth = [list(map(int, input().split())) for _ in range(N)]

for zero, one, two in growth:
    grow = [0]*zero + [1]*one + [2]*two

    for i in range(M):
        honeycomb[M-i-1][0] += grow[i]
        if M-i-1:
            honeycomb[0][M-i-1] += grow[-i-1]

for r in range(1, M):
    for c in range(1, M):
        honeycomb[r][c] = honeycomb[r-1][c]

[print(*h) for h in honeycomb]
