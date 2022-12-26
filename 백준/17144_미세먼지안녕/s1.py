import sys
sys.stdin = open('input.txt')


R, C, T = map(int, input().split())
room = []
for _ in range(R):
    input_line = list(map(int, input().split()))
    room.append(input_line)

for r in range(2, R):
    if room[r][0] == -1:
        cleaner_row1 = r
        cleaner_row2 = r + 1
        break


def dust(graph):
    tmp = [[0] * C for _ in range(R)]
    tmp[cleaner_row1][0] = -1
    tmp[cleaner_row2][0] = -1
    for r in range(R):
        for c in range(C):
            if graph[r][c] > 0:
                cnt = 0
                for dr, dc in [[-1,0], [0,-1], [0,1], [1,0]]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] != -1:
                        cnt += 1
                        tmp[nr][nc] += graph[r][c] // 5
                tmp[r][c] += graph[r][c] - (cnt * (graph[r][c] // 5))
                tmp[r][c] = max(0, tmp[r][c])
    return tmp

def cleanup(graph, row1, row2):
    for r in range(row1-1, -1, -1):
        graph[r][0] = graph[r-1][0]
    for c in range(C-1):
        graph[0][c] = graph[0][c+1]
    for r in range(row1):
        graph[r][C-1] = graph[r+1][C-1]
    for c in range(C-1, 0, -1):
        graph[row1][c] = graph[row1][c-1]

    for r in range(row2+1, R-1):
        graph[r][0] = graph[r+1][0]
    for c in range(C-1):
        graph[R-1][c] = graph[R-1][c+1]
    for r in range(R-1, row2-1, -1):
        graph[r][C-1] = graph[r-1][C-1]
    for c in range(C-1, 0, -1):
        graph[row2][c] = graph[row2][c-1]

    graph[row1][1], graph[row2][1] = 0, 0


for _ in range(T):
    room = dust(room)
    cleanup(room, cleaner_row1, cleaner_row2)
    [print(g) for g in room]

res = 2
for row in room:
    res += sum(row)
print(res)

