import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
que = list(range(1, n+1))
answer = []

while que:
    for _ in range(k-1):
        que.append(que.pop(0))
    answer.append(que.pop(0))

print('<', end='')
print(*answer, sep=', ', end='')
print('>', end='')