import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(range(1, n+1))
lst = [int(input()) for _ in range(n)]

stack = []
answer = []

tmp = 0
for _ in range(n):
    v = lst.pop(0)

    while tmp < v:
        tmp += 1
        stack.append(tmp)
        answer.append('+')

    if stack[-1] == v:
        stack.pop()
        answer.append('-')
        # print(stack)


if stack:
    answer = 'NO'
    print(answer)
else:
    for a in answer:
        print(a)