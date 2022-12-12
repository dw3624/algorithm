import sys
sys.stdin = open('input.txt')

# 이진 트리의 중위 순회(inorder traversal)와 후위 순회(postorder traversal)가 주어질 때, 이를 전위 순회(preorder traversal)로 출력하는 문제입니다.
# 전위 순회: root → left → right
# 중위 순회: left → root → right
# 후위 순회: left → right → root
#
# 후위 순회에서는 트리의 root를 알 수 있고, 중위 순회에서는 좌우 자식 트리의 정보를 알 수 있습니다.
# 후위 순회의 마지막 원소는 최상위 루트이며, 이를 기준으로 중위 순회를 왼쪽 서브 트리와 오른쪽 서브 트리로 나눌 수 있습니다.
# 예)
# 중위 순회 : 4 2 5  ((1))  6 3 7
# 후위 순회 : 4 5 2 6 7 3  ((1))
# 이 때,
# 중위 순회 왼쪽 서브 트리 범위: 시작 idx~ (시작 idx + 왼쪽 서브 트리 노드 수 -1)
# 중위 순회 오른쪽 서브 트리 범위: (끝 idx - 오른쪽 서브 트리 노드 수 + 1) ~ 끝 idx
# 후위 순회 왼쪽 서브 트리 범위: 시작 idx~ (시작 idx + 왼쪽 서브 트리 노드 수 -1)
# 후위 순회 오른쪽 서브 트리 범위: (끝 idx - 오른쪽 서브 트리 노드 수) ~ (끝 idx - 1)
#

import sys
sys.setrecursionlimit(10**6)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

pos = [0] * (n + 1)
for i in range(n):
    pos[in_order[i]] = i


def solve(in_start, in_end, post_start, post_end):
    if (in_start > in_end) or (post_start > post_end):
        return

    root = post_order[post_end] # 후위 순회에서 부모 노드 찾기
    print(root, end=" ")
    left = pos[root] - in_start # 왼쪽 인자 개수
    right = in_end - pos[root]  # 오른쪽 인자 개수

    # 왼쪽 노드
    solve(in_start, in_start+left-1, post_start, post_start+left-1)
    # 오른쪽 노드
    solve(in_end-right+1, in_end, post_end-right, post_end-1)


solve(0, n-1, 0, n-1)
