# 벨만-포드 알고리즘을 이용해 푸는 문제입니다.
# 벨만-포드 알고리즘은 최단 거리 검색 알고리즘입니다.
# 가중치가 음수여도 최단거리를 구할 수 있다는 특징이 있습니다.
# 반면, 매번 각 노드에서 모든 경로를 탐색하기 때문에 시간복잡도가 큰 단점이 있습니다.
# 1. 출발 노드 설정
# 2. 최단 거리 테이블 초기화
# 3. 다음 과정을 N-1번 반복
#   1) 전체 간선 E개 하나씩 확인
#   2) 각 간선 거쳐 다른 노드로 가는 비용 계산, 최단 거리 테이블 갱신


import sys
sys.stdin = open('input.txt')

from collections import defaultdict


def bellman_ford(start):
    dist[start] = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            for nn, time in nodes[j]:
                if dist[nn] > dist[j] + time:
                    dist[nn] = dist[j] + time
                    # n번 이후 값이 갱신된다면 음수 순환 존재
                    if i == n:
                        return True
    return False


tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    nodes = defaultdict(list)
    dist = [1e9] * (n + 1)
    for _ in range(m):
        s, e, t = map(int, input().split())
        nodes[s].append((e, t))
        nodes[e].append((s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        nodes[s].append((e, -t))


    negative_cycle = bellman_ford(1)
    if negative_cycle:
        print('YES')
    else:
        print('NO')