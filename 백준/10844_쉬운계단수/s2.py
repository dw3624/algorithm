import sys
sys.stdin = open('input.txt')

N = int(input())

# row : 자릿수,  col : 0 ~ 9
# dp[row][col] : row자릿수 숫자에서 col숫자 나오는 횟수
dp = [[0]*10 for _ in range(N+1)]

# 1 자리 수 모두 1로 초기화
for c in range(1, 10):
    dp[1][c] = 1

# 2 자리 수 이상
# dp[N 자릿수][N 자릿수일때 일의 자리 수]
for r in range(2, N+1):
    for c in range(10):
        if c == 0:
            dp[r][c] = dp[r-1][c+1]
        elif c == 9:
            dp[r][c] = dp[r-1][c-1]
        else:
            dp[r][c] = dp[r-1][c-1] + dp[r-1][c+1]
# [print(d) for d in dp]
print(sum(dp[-1]) % 1000000000)