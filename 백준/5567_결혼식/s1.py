# 트리 구조를 사용해 해결할 수 있는 문제입니다.
# 트리를 생성해 두번째 depth까지 탐색, 1번 노드와 연결된 노드 수를 규합니다.
#   - 1번 노드: 상근이
#   - 첫 번째 depth: 상근이 친구
#   - 두 번째 depth: 상근이 친구의 친구
# 1. 입력값으로 트리 생성
# 2. 트리 탐색
#   1) que 생성 (1의 자식 노드로 초기화)
#   2) pop한 노드의 자식 노드 순환
#   3) depth가 2를 넘어갈 경우 종료
#   4) 아닌 경우 해당 노드 기록 후 push


import sys
sys.stdin = open('input.txt')


from collections import defaultdict


n = int(input())
m = int(input())
tree = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

friends = [0] * (n + 1)
friends[1] = 1
q = []
depth = 0
for node in tree[1]:
    q.append((node, depth))

while q:
    now, depth = q.pop(0)

    if depth >= 2:
        continue

    friends[now] = 1
    for node in tree[now]:
        if node > 1:
            q.append((node, depth + 1))

res = friends.count(1) - 1
print(res)