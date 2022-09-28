import sys
sys.stdin = open('input.txt')

def bfs(n, k):
    visit_time = [-1] * 100001
    visit_time[n] = 0
    q = [n]
    while q:
        x = q.pop(0)
        if x == k:
            return visit_time[x]
        if 0 < x * 2 < 100001 and visit_time[x * 2] == -1:
            # 곱셈 연산 우선 시키기 위함
            q.insert(0, x * 2)
            visit_time[x * 2] = visit_time[x]
        if 0 <= x + 1 < 100001 and visit_time[x + 1] == -1:
            q.append(x + 1)
            visit_time[x + 1] = visit_time[x] + 1
        if 0 <= x - 1 < 100001 and visit_time[x - 1] == -1:
            q.append(x - 1)
            visit_time[x - 1] = visit_time[x] + 1
    return


N, K = map(int, input().split())
res = bfs(N, K)
print(res)


N, K = map(int, input().split())
res = bfs(N, K)
print(res)