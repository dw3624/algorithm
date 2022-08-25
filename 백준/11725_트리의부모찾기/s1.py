import sys
sys.stdin = open('input.txt')


from collections import deque
import sys

N = int(input())
node_set = [list(map(int, sys.stdin.readline().split())) for _ in range(N-1)]
node_dict = {}
for n in node_set:
    node_dict.setdefault(n[0], []).append(n[1])
    node_dict.setdefault(n[1], []).append(n[0])

q = deque([1])
nodes = [0]*(N+1)
while q:
    v = q.popleft()
    for child in node_dict[v]:
        if nodes[v] != child:
            nodes[child] = v
            q.append(child)
print(*nodes[2:], sep='\n')






