import sys
sys.stdin = open('input.txt')

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    mat = [input() for _ in range(N)]
    visit = [[987654321] * M for _ in range(N)]

    que = deque()
    # que = [0] * (N * M)
    # front, rear = -1, -1


    for r in range(N):
        for c in range(M):
            if mat[r][c] == 'W':
                que.append([r, c])
                # rear += 1
                # que[rear] = [r, c]
                visit[r][c] = 0
    # print(que)


    while que:
    # while front != rear:
        r, c = que.popleft()
        # front += 1
        # r, c = que[front]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if mat[nr][nc] == 'L' and visit[nr][nc] == 987654321:
                visit[nr][nc] = visit[r][c] + 1
                que.append([nr, nc])
                # rear += 1
                # que[rear] = [nr, nc]
    # print(visit)


    answer = 0
    for v1 in visit:
        for v2 in v1:
            answer += v2
    print('#{} {}'.format(tc, answer))