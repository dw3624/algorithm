import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start+end) // 2

    tmp = 0
    for tree in trees:
        if tree >= mid:
           tmp += tree-mid

    if tmp >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)