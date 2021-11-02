import sys
sys.stdin = open('input.txt')

N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

# 부분집합의 원소 개수 (1<<N = 2^N)
for i in range(1, 1<<N):
    tmp = 0

    # 각 인덱스 번호 - 해당 인덱스의 숫자가 부분집합에 포함/미포함
    for j in range(N):
        if i & (1<<j):
            # print(nums[j], end=' ')
            tmp += nums[j]

    # print(tmp)
    if tmp == S:
        cnt += 1
    # print()

print(cnt)


