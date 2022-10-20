import sys
sys.stdin = open('input.txt')


def bfs(sr, sc, gr, gc):
    visit = [[0] * i for _ in range(i)]
    q = [(sr, sc, 0)]
    while q:
        r, c, cnt = q.pop(0)
        if r == gr and c == gc:
            print(cnt)
            return
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < i and 0 <= nc < i and not visit[nr][nc]:
                visit[nr][nc] = 1
                q.append((nr, nc, cnt + 1))


t = int(input())
dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [-2, -1, 1, 2, 2, 1, -1, -2]
for _ in range(t):
    i = int(input())
    mat = [[0] * i for _ in range(i)]
    sr, sc = map(int, input().split())
    gr, gc = map(int, input().split())
    bfs(sr, sc, gr, gc)
