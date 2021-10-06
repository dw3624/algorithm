import sys
sys.stdin = open('input.txt')


def f(n):
    global tmp

    if n == M:
        print(*tmp)
        return

    for i in range(N):
        if not used[i]:
            used[i] += 1
            tmp.append(nums[i])

            f(n+1)

            used[i] -= 1
            tmp.pop()


N, M = map(int, input().split())
nums = list(range(1, N+1))
used = [0]*N
tmp = []
f(0)