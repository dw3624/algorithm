import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
cache = [0]*(K+1)
for _ in range(N):
    w, v = map(int, input().split())
    for i in range(K, w-1, -1):
        cache[i] = max(cache[i], cache[i-w] + v)
    print('w:', w, 'v:', v, cache)
print(cache[-1])