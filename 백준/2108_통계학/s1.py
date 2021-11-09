import sys
sys.stdin = open('input.txt')


def mode_num():
    # 숫자가 하나밖에 없는 경우
    if len(nums) == 1:
        return nums[0]

    # 숫사별로 몇번 나왔는지 카운트
    cnts = {}
    for num in nums:
        cnts[num] = cnts.get(num, 0) + 1

    # 최대 등장 수
    max_cnt = max(cnts.values())

    # 숫자들이 등장한 횟수가 최대 등장 수와 같은 경우 tmp list에 추가
    tmp = []
    for cnt in cnts:
        if cnts.get(cnt) == max_cnt:
            tmp.append(cnt)

    # 최빈값이 1개인 경우
    if len(tmp) == 1:
        return tmp[0]
    # 최빈값이 여러개인 경우
    else:
        tmp.sort()
        return tmp[1]


N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

n1 = round(sum(nums)/N)
n2 = nums[N//2]
n3 = mode_num()
n4 = nums[-1] - nums[0]

print(n1)
print(n2)
print(n3)
print(n4)