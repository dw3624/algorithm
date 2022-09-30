import sys
sys.stdin = open('input.txt')

n = int(input())
num = [int(input()) for _ in range(n)]

if n <= 2:
    print(sum(num))
else:
    dp = num[:2] + [0] * 10000
    for i in range(1, n):
            dp[i] = max(num[i]+num[i-1]+dp[i-3], num[i]+dp[i-2])
            dp[i] = max(dp[i-1], dp[i])
    print(max(dp))