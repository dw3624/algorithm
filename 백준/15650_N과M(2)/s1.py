import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())

def back(idx, depth, nums):
    if depth == M:
        print(*nums)
        return
    for i in range(idx+1, N+1):
        nums.append(i)
        back(i, depth+1, nums)
        nums.pop()

back(0, 0, [])