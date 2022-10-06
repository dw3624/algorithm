import sys
sys.stdin = open('input.txt')


#   1 2 3  4  5 6 7 8  9  10
# 1 1 1 1  1  1 1 1 1  1  1
# 2 1 2 2  3  3 4 4 5 [5] 6
# 5 1 2 2 [3] 4 5 6 7 [8] 10

# 예를 들어 1,2,5 사용해 8 만들 경우
# 1,2 사용해 8 만드는 경우 + 5 사용해 8 만드는 경우
# 5 사용해 8 만드는 경우, 5를 최소 1개 사용하기 떄문에 8-5의 경우의 수 사용
# dp[5][8] = dp[2][8] + dp[5][8-5]

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1
for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]
print(dp[-1])



