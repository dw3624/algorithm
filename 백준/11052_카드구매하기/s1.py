import sys
sys.stdin = open('input.txt')


n = int(input())
ps = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(1, n+1):
    for j in range(i, i//2-1, -1):
        dp[i] = max(ps[i], dp[j] + dp[i-j], dp[i])
print(dp[-1])

