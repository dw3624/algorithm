import sys
sys.stdin = open('input.txt')


dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def work(r, c, h, road, skill):
    global ans
    if road > ans: ans = road
    visit[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N or visit[nr][nc]: continue
        if h > mat[nr][nc]:
            work(nr, nc, mat[nr][nc], road + 1, skill)
        elif skill and h > mat[nr][nc] - K:
            work(nr, nc, mat[r][c] - 1, road + 1, 0)
    visit[r][c] = 0



T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*(N) for _ in range(N)]

    max_h = 0
    ans = 0
    for i in range(N):
        for j in range(N):
            if max_h < mat[i][j]:
                max_h = mat[i][j]


    for r in range(N):
        for c in range(N):
            if mat[r][c] == max_h:
                work(r, c, max_h, 1, 1)

    print('#{} {}'.format(tc, ans))


