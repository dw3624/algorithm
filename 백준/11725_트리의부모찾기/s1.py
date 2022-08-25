import sys
sys.stdin = open('input.txt')

N = int(input())

# 1-6-3-5
#  ㄴ4-2
#    ㄴ7

# 1 6 4
# 2 4
# 3 6 5
# 4 1 2 7
# 5 3
# 6 1 3
# 7 4
node_set = [list(map(int, input().split())) for _ in range(N-1)]
node_lst = [[] for _ in range(N+1)]

for n in node_set:
    node_lst[n[0]].append(n[1])
    node_lst[n[1]].append(n[0])
print(node_lst)

node_dict = {}


