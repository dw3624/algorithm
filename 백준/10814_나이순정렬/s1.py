import sys
sys.stdin = open('input.txt')

N = int(input())
lst = []

for _ in range(N):
    tmp = list(input().split())
    # int type으로 지정해야 정렬 제대로 됨
    tmp[0] = int(tmp[0])
    lst.append(tmp)
lst = sorted(lst, key=lambda x:(x[0]))

[print(*l) for l in lst]