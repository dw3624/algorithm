import sys
sys.stdin = open('input.txt')

# 시간초과
# def bfs(r, c):
#     que = [0] * 1000000
#     front = rear = -1
#
#     rear += 1
#     que[rear] = (r, c)
#
#     while front != rear:
#         front += 1
#         r, c = que[front]
#
#         for d in range(4):
#             nr = r + dr[d]
#             nc = c + dc[d]
#             if 0 <= nr < N and 0 <= nc < M \
#                     and mat[nr][nc] and not visit[nr][nc]:
#                 visit[nr][nc] = 1
#                 rear += 1
#                 que[rear] = (nr, nc)


from collections import deque

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(r, c):
    que = deque()
    que.append((r, c))

    while que:
        r, c = que.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and mat[nr][nc] and not visit[nr][nc]:
                visit[nr][nc] = 1
                que.append((nr, nc))


T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    mat = [[0]*(M) for _ in range(N)]
    visit = [[0]*(M) for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        mat[y][x] = 1
    # [print(m) for m in mat]

    ans = 0
    for r in range(N):
        for c in range(M):
            if mat[r][c] and not visit[r][c]:
                bfs(r, c)
                ans += 1
    print(ans)