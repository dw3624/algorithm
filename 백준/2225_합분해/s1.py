import sys
sys.stdin = open('input.txt')


# dp[k][n]: k개 수 써서 n만들 수 있는 경우의 수
# dp[k][n] = dp[k-1][0] + dp[k-2][1] + ... + dp[k-1][n-0]

n, k = map(int, input().split())
dps = [[0] * (n + 1) for _ in range(k)]

for i in range(n + 1):
    dps[0][i] = 1
for j in range(k):
    dps[j][0] = 1

for r in range(1, k):
    for c in range(1, n + 1):
        dps[r][c] = dps[r-1][c] + dps[r][c-1]

print(dps[-1][-1] % 1000000000)

