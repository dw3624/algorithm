import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

not_heard = set()
not_seen = set()

for _ in range(N):
    not_heard.add(input())
for _ in range(M):
    not_seen.add(input())

not_heard_seen = list(not_heard & not_seen)
not_heard_seen.sort()

print(len(not_heard_seen))
[print(person) for person in not_heard_seen]