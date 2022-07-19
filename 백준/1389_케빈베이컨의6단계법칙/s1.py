import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
relations = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    relations[A].append(B)
    relations[B].append(A)


def bfs(s):
    cnt = 0
    people = [0] * (N + 1)
    people[s] = -1
    q = [(s, cnt)]

    while q:
        p, cnt = q.pop(0)
        for r in relations[p]:
            if not people[r]:
                q.append((r, cnt+ 1))
                people[r] = cnt+1
    return sum(people)+1

res = [0, 1e9]
for i in range(1, N+1):
    total = bfs(i)
    if total < res[1]:
        res[0] = i
        res[1] = total

print(res[0])