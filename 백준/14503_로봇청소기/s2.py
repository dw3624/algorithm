# 런타임 에러 (RecursionError)
import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
sr, sc, d = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 1


def clean(r, c, depth):
    global cnt, d
    # 네 방향 모두 본 뒤
    if depth == 4:
        nr = r + dr[(d + 2) % 4]
        nc = c + dc[(d + 2) % 4]
        # 뒤쪽에 벽이 없는 경우
        if mat[nr][nc] == 2:
            clean(nr, nc, 0)
        # 사방이 막힌 경우
        else:
            print(cnt)
            exit(0)

    # 왼쪽확인
    nr = r + dr[(d + 3) % 4]
    nc = c + dc[(d + 3) % 4]

    if not mat[nr][nc]:
        # 방향 전환
        d = (d + 3) % 4
        mat[nr][nc] = 2
        cnt += 1
        clean(nr, nc, 0)
    elif mat[nr][nc] == 1 or mat[nr][nc] == 2:
        # 방향 전환
        d = (d + 3) % 4
        clean(r, c, depth + 1)


mat[sr][sc] = 2
clean(sr, sc, 0)




