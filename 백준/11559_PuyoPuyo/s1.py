import sys
sys.stdin = open('input.txt')


dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
def bfs(r, c):
    global cnt
    q = [(r, c)]
    chain.append((r, c))

    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < 12 and 0 <= nc < 6\
                    and not visit[nr][nc] and mat[r][c]==mat[nr][nc]:
                q.append((nr, nc))
                chain.append((nr, nc))
                visit[nr][nc] += 1


def down():
    for c in range(6):
        for r1 in range(10, -1, -1):
            for r2 in range(11, r1, -1):
                if mat[r1][c] != '.' and mat[r2][c] == '.':
                    mat[r2][c], mat[r1][c] = mat[r1][c], mat[r2][c]
                    break


mat = [list(map(str, input())) for _ in range(12)]
combo = 0
while True:
    isTrue = False
    visit = [[0]*(6) for _ in range(12)]
    for r in range(12):
        for c in range(6):
            if mat[r][c] != '.' and not visit[r][c]:
                visit[r][c] += 1
                chain = []
                bfs(r, c)

                if len(chain) >= 4:
                    isTrue = True
                    for cr, cc in chain:
                        mat[cr][cc] = '.'

    if not isTrue: break

    down()
    combo += 1
print(combo)

