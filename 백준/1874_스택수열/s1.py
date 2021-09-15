import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(range(1, n+1))
lst = [int(input()) for _ in range(n)]

stack = []
answer = []

i = 0
v = lst.pop(0)

while lst:
    i %= 8
    print(nums[i], v, lst)
    print(stack)
    if stack and stack[-1] == v:
        answer.append('-')
        stack.pop()
        v = lst.pop(0)
        i -= 1

    elif nums[i] != v:
        answer.append('+')
        stack.append(nums[i])

    elif nums[i] == v:
        answer.append('+')
        stack.append(nums[i])

    i += 1
    print(stack)
    print()

#
# for a in answer:
#     print(a)