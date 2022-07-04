import sys
sys.stdin = open('input.txt')


def dfs(sr, sc, cnt, total):
    global res
    # 가지치기
    if res >= total + (4-cnt)*max_mat:
        return
    # 폴리오미노 완성시 함수 종료
    if cnt >= 4:
        res = max(total, res)
        return

    for dr, dc in [(0,-1), (0,1), (-1,0), (1,0)]:
        nr, nc = sr+dr, sc+dc
        if 0<=nr<N and 0<=nc<M and not visit[nr][nc]:
            # T자 모양 탐색
            if cnt == 2:
                visit[nr][nc] = 1
                dfs(sr, sc, cnt+1, total+mat[nr][nc])
                visit[nr][nc] = 0
            # 기타 모양 탐색
            visit[nr][nc] = 1
            dfs(nr, nc, cnt + 1, total + mat[nr][nc])
            visit[nr][nc] = 0


N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
max_mat = max(map(max, mat))

res = 0
for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 1, mat[r][c])
        visit[r][c] = 0
print(res)