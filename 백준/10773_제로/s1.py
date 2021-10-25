import sys
sys.stdin = open('input.txt')

K = int(input())
ans = []
for _ in range(K):
    k = int(input())
    if k:
        ans.append(k)
    else:
        ans.pop()

print(sum(ans))