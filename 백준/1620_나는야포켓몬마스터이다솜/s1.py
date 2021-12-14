import sys
sys.stdin = open('input.txt')

# .index(), in 등 list 반복문을 여러번 사용하는 것 보다
# dict 등을 활용하는것이 속도면에서 더 효율적임


import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pkmn_list = [0] * (N+1)
pkmn_dict = {}

for n in range(1, N+1):
    pkmn = input().rstrip()
    pkmn_list[n] = pkmn
    pkmn_dict[pkmn] = n

for _ in range(M):
    quiz = input().rstrip()
    if quiz.isdigit():
        print(pkmn_list[int(quiz)])
    else:
        print(pkmn_dict[quiz])