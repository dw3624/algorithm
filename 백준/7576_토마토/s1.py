import sys
sys.stdin = open('input.txt')

from collections import deque

dr = [0,0,-1,1]
dc = [-1,1,0,0]

def bfs():
    global cnt

    while que:
        # cnt : 지난 일수
        cnt += 1
        # print(cnt, que)

        # que 길이만큼 반복 > depth별 cnt횟수 알 수 있음
        for _ in range(len(que)):
            r, c = que.popleft()

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                # 범위내, 미방문, 토마토만 있는 곳만 방문
                if 0<=nr<N and 0<=nc<M\
                        and not visit[nr][nc] and -1<mat[nr][nc]:
                    que.append((nr, nc))
                    visit[nr][nc] = 1
    # print(cnt)


M, N = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
# [print(m) for m in mat]

que = deque()
for r in range(N):
    for c in range(M):
        # 토마토 있는경우, visit 기록, que 추가
        if mat[r][c] == 1:
            que.append((r,c))
            visit[r][c] = 1

        # 토마토 없는경우, visit 기록
        elif mat[r][c] == -1:
            visit[r][c] = 1

cnt = -1
bfs()

# 미방문한 토마토칸이 있으면 -1
for r in range(N):
    for c in range(M):
        if not visit[r][c]:
            cnt = -1
            break

print(cnt)
