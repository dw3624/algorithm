import sys
sys.stdin = open('input.txt')


def dfs(s):
    visit[s] = 1
    print(s, end=' ')
    for i in range(1, N+1):
        if not visit[i] and nodes[s][i]:
            dfs(i)

def bfs(s):
    que = [s]
    visit[s] = 1

    while que:
        v = que.pop(0)
        print(v, end=' ')
        for i in range(1, N+1):
            if not visit[i] and nodes[v][i]:
                que.append(i)
                visit[i] = 1




N, M, V = map(int, input().split())
nodes = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    m1, m2 = map(int, input().split())
    nodes[m1][m2] = nodes[m2][m1] = 1


# nodes = {}
# for _ in range(M):
#     m1, m2 = map(int, input().split())
#     nodes.setdefault(m1, []).append(m2)

visit = [0]*(N+1)
dfs(V)
print()
visit = [0]*(N+1)
bfs(V)