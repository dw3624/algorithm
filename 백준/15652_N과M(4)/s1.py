import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

def back(idx, cnt, nums):
    if cnt == M:
        return print(*nums)
    for i in range(idx, N):
        nums.append(i+1)
        back(i, cnt+1, nums)
        nums.pop()

back(0, 0, [])