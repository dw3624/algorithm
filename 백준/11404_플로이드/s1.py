import sys
sys.stdin = open("input.txt")


n = int(input())
m = int(input())
costs = [[100001 for _ in range(n + 1)] for _ in range(n + 1)]
for r in range(1, n + 1):
    for c in range(1, n + 1):
        if r == c:
            costs[r][c] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    costs[a][b] = min(c, costs[a][b])

for i in range(1, n + 1):
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if r != c:
                costs[r][c] = min(costs[r][c], costs[r][i] + costs[i][c])

for r in costs[1:]:
    for c in r[1:]:
        if c == 100001:
            print(0, end=" ")
        else:
            print(c, end=" ")
    print()
