import sys
sys.stdin = open('input.txt')

n = int(input())
dp = [0]*(n+1)    # 최소제곱수 개수 저장
dp[1] = 1

for i in range(2, n+1):
    '''
    dp[i]의 최소제곱수 개수 : 
        자신(i)보다 작거나 같은 제곱수 탐색, 1 추가
        => dp[i-(j**2)] + 1

    i가 27인 경우 : 
        dp[27-(5**2)] + 1 => dp[2] + 1 => 2 + 1 => 3
    '''

    val = 1e9   # 1e9 == 1*(10**9)
    j = 1
    while (j**2) <= i:
        val = min(val, dp[i-(j**2)])
        j += 1
    dp[i] = val + 1

print(dp[n])