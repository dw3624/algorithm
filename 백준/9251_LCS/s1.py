import sys
sys.stdin = open('input.txt')


#   a c a y k p
# c 0 1 1 1 1 1
# a 1 1 2 2 2 2
# p 1 1 2 2 2 3
# c 1 2 2 2 2 3
# a 1 2 3 3 3 3
# k 1 2 3 3 4 4


word1, word2 = input(), input()
cache = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]

for i in range(1, len(word2)+1):
    for j in range(1, len(word1)+1):
        if word1[j-1] == word2[i-1]:
            cache[i][j] = cache[i-1][j-1] + 1
        else:
            cache[i][j] = max(cache[i-1][j], cache[i][j-1])
print(cache[-1][-1])


