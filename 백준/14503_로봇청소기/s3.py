import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
r, c, d = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
visit[r][c] = 1
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 1

while True:
    flag = 0
    for _ in range(4):
        # 왼쪽확인
        nr = r + dr[(d + 3) % 4]
        nc = c + dc[(d + 3) % 4]
        d = (d + 3) % 4
        if 0 <= nr < n and 0 <= nc < m and not mat[nr][nc]:
            if not visit[nr][nc]:
                visit[nr][nc] = 1
                cnt += 1
                r, c = nr, nc
                flag = 1
                break

    # 네 방향 모두 본 뒤
    if not flag:
        # 사방이 막힌 경우
        if mat[r - dr[d]][c - dc[d]] == 1:
            print(cnt)
            break
        # 뒤쪽에 벽이 없는 경우
        else:
            r, c = r - dr[d], c - dc[d]


