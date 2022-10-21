import sys
sys.stdin = open('input.txt')


def check(word):
    used = {}
    for i in range(1, len(word)):
        if word[i-1] == word[i]:
            pass
        else:
            if used.get(word[i-1]):
                return 0
            else:
                used[word[i-1]] = 1
    return 1


n = int(input())
res = 0
for _ in range(n):
    word = input() + ' '
    res += check(word)
print(res)