import sys
sys.stdin = open('input.txt')

N = int(input())
students = [list(map(int, input().split())) for _ in range(N)]

ranks = []
for _ in range(N):
    s = students.pop(0)
    tmp_rank = 1
    for student in students:
        if s[0] < student[0] and s[1] < student[1]:
            tmp_rank += 1
    students.append(s)
    ranks.append(tmp_rank)

print(*ranks)