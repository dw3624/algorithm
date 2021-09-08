import sys
sys.stdin = open('input.txt')

T = int(input())
N = int(input())


# 1 ~ 99 > 99개
# 한자릿수, 두자릿수 모두 한수
# 100 ~
# 각 자릿수별 차이가 같으면 한수
# 예) 123
## 1-2 = 2-3


def hansu(num):
    if 0 < num < 100:
        result = num
        return result

    result = 99
    for n in range(100, num+1):
        nums = list(map(int, str(n)))
        if nums[0] - nums[1] == nums[1] - nums[2]:
            result += 1

    return result

print(hansu(N))