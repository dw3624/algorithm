import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    dp[0][0], dp[1][0] = stickers[0][0], stickers[1][0]

    for i in range(1, n):
        if i > 1:
            dp[0][i] = max(dp[1][i-1] + stickers[0][i],
                           dp[1][i-2] + stickers[0][i])
            dp[1][i] = max(dp[0][i-1] + stickers[1][i],
                           dp[0][i-2] + stickers[1][i])
        else:
            dp[0][i] = dp[1][i - 1] + stickers[0][i]
            dp[1][i] = dp[0][i - 1] + stickers[1][i]
    res = max(dp[0][-1], dp[1][-1])
    print(res)