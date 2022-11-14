import sys
sys.stdin = open('input.txt')


n, k = map(int, input().split())
cnts = [0] + [10001] * k
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort()
for coin in coins:
    for i in range(coin, k + 1):
        cnts[i] = min(cnts[i], cnts[i - coin] + 1)

if cnts[-1] > 10000:
    print(-1)
else:
    print(cnts[-1])