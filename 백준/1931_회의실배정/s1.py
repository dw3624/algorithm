import sys
sys.stdin = open('input.txt')

N = int(input())
I = [list(map(int, input().split())) for _ in range(N)]
I = sorted(I, key=lambda x: [x[1], x[0]])

e = 0
cnt = 0
for i in I:
    if e <= i[0]:
        e = i[1]
        cnt += 1
        print(i)
print(cnt)