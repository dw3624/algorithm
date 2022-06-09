import sys
sys.stdin = open('input.txt')

T = int(input())
stairs = [0]
for _ in range(T):
    stairs.append(int(input()))

scores = [0] * (T+1)
for i in range(1, T+1):

    t1 = stairs[i] + stairs[i-1] + scores[i-3]
    t2 = stairs[i] + scores[i-2]
    if t1 > t2:
        scores[i] = t1
    else:
        scores[i] = t2

print(scores[-1])