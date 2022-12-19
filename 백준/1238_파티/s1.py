import sys
sys.stdin = open('input.txt')

# 다익스트라를 사용하는 문제입니다.
# 특정 지점에서 다른 특정 지점까지의 최단 경로 구하는 알고리즘
# 1. 출발 노드 설정
# 2. 최단 거리 테이블 초기화
# 3. 미방문 노드 중 최단거리 가장 짧은 노드 선택
# 4. 해당 노드 거쳐 다른 노드로 가는 비용 계산, 최단 거리 테이블 업데이트
# 5. 3~4번 반복

# 1. 각 노드를 출발점으로 다익스트라
# 2. x번 노드를 출발점으로 다익스트라
# 3. 위 둘 합친 값의 최댓값과 답 비교 후 갱신
# for 노드 in 모든 노드(1~n):
#   a = 다익스트라(노드)[x]
#   b = 다익스트라(x)[노드]
#   ans = max(a + b, ans)


from collections import defaultdict
from heapq import heappop, heappush


n, m, x = map(int, input().split())
nodes = defaultdict(list)
for _ in range(m):
    s, g, t = map(int, input().split())
    nodes[s].append((g, t))


def dijkstra(start):
    # 각 노드간 거리 초기화 (출발 노드 0 설정)
    dists = [1e9] * (n + 1)
    dists[start] = 0
    q = []
    heappush(q, (0, start))

    while q:
        dist, now = heappop(q)

        #  입력된 값이 더 작은 경우 다음 노드로
        if dists[now] < dist:
            continue

        # 연결된 노드 탐색
        for i, cost in nodes[now]:
            # 연결된 노드 거쳐간 값이 더 작은 경우 갱신, que 추가
            if dist + cost < dists[i]:
                dists[i] = dist + cost
                heappush(q, (dist + cost, i))

    return dists

res = 0
for i in range(1, n + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    res = max(res, go[x] + back[i])
print(res)