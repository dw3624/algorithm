import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)
from collections import defaultdict

n = int(input())
graph = defaultdict(list)
for i in range(n):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
visited = [0 for _ in range(n + 1)]
circle = list()
finded = -1


def FindCycle(u, tar):
    # finded 변수는 공급 물탱크와 방문 여부를 확인하기 위한 변수입니다.
    global finded
    # 방문 기록이 있다면, 순환구조라고 할 수 있다.
    # 순환되는 고리는 단 1개이기 때문이다.
    if visited[u] == 1:
        finded = u
        if u not in circle:
            circle.append(u)
        # 방문 기록이 없다면, 방문 기록을 남긴다. Visited변수는 방문 기록을 남긴다.
        return
    # 도착한 물탱크(노드)에서 갈 수 있는 물탱크들로 물을 보낸다.
    visited[u] = 1
    for i in graph[u]:
        # 만약에 i값이 이전의 공급한 물탱크면 탐색 정지
        if i == tar:
            continue
        # 방문한 적 없고, 공급한 물탱크가 아니라면 새로운 탐색지점으로 잡는다.
        # 즉, 새로운 재귀 시작 지점이 된다.
        FindCycle(i, u)
        # 이미 발견된 순환 고리 값이라면 탐색 정지
        if finded == -2:
            return
        # finded = u라면 이미 방문 지점이기때문에 탐색 정지
        if finded == u:
            finded = -2
            return

        # 새롭게 발견한 순환 고리 값이라면 순환 고리에 추가하고, 탐색 종료
        if finded >= 0:
            if u not in circle:
                circle.append(u)
            return


FindCycle(1, 1)
circle.sort()
print(len(circle))
for i in circle:
    print(i, end=" ")
