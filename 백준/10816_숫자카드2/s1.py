import sys
sys.stdin = open('input.txt')

N = int(input())
n_nums = list(map(int, input().split()))
M = int(input())
m_nums = list(map(int, input().split()))

num_dict = {}
for n_num in n_nums:
    num_dict[n_num] = num_dict.get(n_num, 0) + 1

answer = [0] * M
for i in range(len(m_nums)):
    m_key = m_nums[i]
    answer[i] = num_dict.get(m_key, 0)

print(*answer)
