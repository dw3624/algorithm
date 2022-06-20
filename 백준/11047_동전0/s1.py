import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
A = []
for _ in range(N):
    a = int(input())
    if a > K:
        break
    A.append(a)

cnt = 0
while K:
    v = A.pop()
    c = K // v
    if c >= 1:
        cnt += c
        K -= v*c
    # print('v:',v, 'c:', c, 'cnt:',cnt,'K:',K)
print(cnt)