import sys
sys.stdin = open('input.txt')


dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def dfs(r, c):
    global tmp

    # print(r, c)
    visit[r][c] += 1
    tmp += 1

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0<=nr<N and 0<=nc<N\
                and mat[nr][nc] and not visit[nr][nc]:
            dfs(nr, nc)


N = int(input())
mat = [list(map(int, input())) for _ in range(N)]
visit = [[0]*N for _ in range(N)]
# [print(m) for m in mat]

result = []
for r in range(N):
    for c in range(N):
        if mat[r][c] and not visit[r][c]:
            tmp = 0
            dfs(r, c)
            result.append(tmp)

result.sort()
print(len(result))
[print(r) for r in result]