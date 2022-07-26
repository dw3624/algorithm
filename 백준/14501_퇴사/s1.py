import sys
sys.stdin = open('input.txt')

N = int(input())
T, P = [], []
dp = [0] * (N+1)
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N-1, -1, -1):
    if T[i] + i > N:
        dp[i] = dp[i+1]
    else:
        # i+1번째 날 기준 수익, i번째 날 수익 + Ti만큼 지난 후 수익 비교
        dp[i] = max(dp[i+1], P[i]+dp[i+T[i]])

    print('T:', T)
    print('P:', P)
    print('dp:', dp)
    print()
print(dp[0])