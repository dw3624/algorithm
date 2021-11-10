import sys
sys.stdin = open('input.txt')

from collections import deque

N = int(input())
que = deque()

for n in range(N):
	que.append(n+1)

while len(que) > 1:
	que.popleft()

	q = que.popleft()
	que.append(q)

print(que.pop())