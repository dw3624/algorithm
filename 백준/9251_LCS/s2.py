import sys
sys.stdin = open('input.txt')

#   a c a y k p
# c 0 1 0 0 0 0
# a 1 1 2 0 0 0
# p 1 1 2 0 0 3
# c 1 2 2 0 0 3
# a 1 2 3 0 0 3
# k 1 2 3 0 4 3

word1, word2 = input(), input()
cache = [0]*(len(word1))

for i in range(len(word2)):
    cnt = 0
    for j in range(len(word1)):
        if cnt < cache[j]:
            cnt = cache[j]
        elif word1[j] == word2[i]:
            cache[j] = cnt + 1
print(max(cache))