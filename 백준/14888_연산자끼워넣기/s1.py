import sys
sys.stdin = open('input.txt')


def cal(i, total):
    global res1, res2

    if i == n - 1:
        res1 = max(res1, total)
        res2 = min(res2, total)
        return

    if cnts[0] and used[0] < cnts[0]:
        used[0] += 1
        cal(i + 1, total + nums[i + 1])
        used[0] -= 1

    if cnts[1] and used[1] < cnts[1]:
        used[1] += 1
        cal(i + 1, total - nums[i + 1])
        used[1] -= 1

    if cnts[2] and used[2] < cnts[2]:
        used[2] += 1
        cal(i + 1, total * nums[i + 1])
        used[2] -= 1

    if cnts[3] and used[3] < cnts[3]:
        used[3] += 1
        tmp = -(-total // nums[i + 1]) if total < 0 else total // nums[i + 1]
        cal(i + 1, tmp)
        used[3] -= 1


n = int(input())
nums = list(map(int, input().split()))
cnts = list(map(int, input().split()))
used = [0] * 4
res1, res2 = -1e9, 1e9
cal(0, nums[0])
print(res1)
print(res2)