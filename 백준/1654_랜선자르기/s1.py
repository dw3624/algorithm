import sys
sys.stdin = open('input.txt')


K, N = map(int, input().split())
nums = [int(input()) for _ in range(K)]

start = 1
end = max(nums)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for num in nums:
        lines += num // mid

    if lines < N:
        end = mid - 1
    elif lines >= N:
        start = mid + 1

print(end)

# lines가 N 이상 => 최소 start 길이만큼
# 여기에 추가로 얼마나 허용되는지 mid로 계산

# -------(start)----(mid)----(end)-----
# mid로 랜선 나눴을 때 lines가 N 이상인 경우,
## 랜선의 최대 길이는 최소한 start 이상
# mid로 랜선 나눴을 때 lines가 N 미만인 경우,
## end를 조금씩 줄여나감
