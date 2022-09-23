import sys
sys.stdin = open("input.txt")


n = int(input())
m = int(input())
graph = [[int(1e9)]*(n+1) for _ in range(n + 1)]

for a in range(1, n + 1):
    graph[a][a] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])

for i in range(1, n + 1):
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            graph[r][c] = min(graph[r][c], graph[r][i] + graph[i][c])

for r in range(1, n+1):
    for c in range(1, n+1):
        if graph[r][c] == int(1e9):
            print(0, end=" ")
        else:
            print(graph[r][c], end=" ")
    print()
