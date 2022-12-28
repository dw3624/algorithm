# 큐를 사용해 해결할 수 있는 문제입니다.
# 주어진 수에 대해 가능한 경우를 각각 계산해 횟수와 함께 큐에 추가합니다.

import sys
sys.stdin = open('input.txt')


a, b = map(int, input().split())
q = [(a, 1)]
while q:
    a, t = q.pop()
    if a == b:
        print(t)
        break
    if a < b:
        q.append((a * 2, t + 1))
        q.append((a * 10 + 1, t + 1))

else:
    print(-1)