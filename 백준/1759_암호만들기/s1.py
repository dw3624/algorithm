import sys
sys.stdin = open('input.txt')


def check(word):
    v_cnt, cnt = 0, 0
    for w in word:
        if w in ['a', 'e', 'i', 'o', 'u']:
            v_cnt += 1
        else:
            cnt += 1
        if v_cnt >= 1 and cnt >= 2:
            return print(word)
    else: return


def back(j, word):
    if len(word) == l:
        return check(word)
    for i in range(j, c):
        back(i+1, word + letters[i])


l, c = map(int, input().split())
letters = list(input().split())
letters.sort()
back(0, '')
