import sys
sys.stdin = open('input.txt')

# N, M = map(int, input().split())
# cards = list(map(int, input().split()))
# result = 0

# for i in range(1<<N):
# 	tmp, cnt = 0, 0
# 	for j in range(N):
# 		if i & (1<<j):
# 			tmp += cards[j]
# 			cnt += 1
# 		if cnt > 3:
# 			break
# 	if cnt == 3 and result < tmp <= M:
# 		result = tmp
		
# print(result)

N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

from itertools import combinations

for card_set in combinations(cards, 3):
	tmp = sum(card_set)
	if result < tmp <= M:
		result = tmp
print(result)