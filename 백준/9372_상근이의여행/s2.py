import sys
sys.stdin = open('input.txt')


def dfs(idx, cnt):
    visit[idx] = 1

    for n in nodes[idx]:
        if not visit[n]:
            cnt = dfs(n, cnt+1)
    return cnt


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    nodes = [[] for _ in range(N+1)]
    visit = [0] * (N+1)

    for i in range(M):
        a, b = map(int, input().split())
        nodes[a].append(b)
        nodes[b].append(a)

    # print(nodes)
    print(dfs(1, 0))