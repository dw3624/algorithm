import sys
sys.stdin = open('input.txt')

N = int(input())
P = list(map(int, input().split()))
P.sort()

result = 0
tmp = 0
for p in P:
    tmp += p
    result += tmp

print(result)