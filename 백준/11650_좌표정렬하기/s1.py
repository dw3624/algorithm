import sys
sys.stdin = open('input.txt')

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst = sorted(lst, key=lambda x: [x[0], x[1]])

for l in lst:
    print(*l)