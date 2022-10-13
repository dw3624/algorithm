import sys
sys.stdin = open('input.txt')


def hanoi(n, frm, assist, to):
    global res
    if n == 1:
        res.append((frm, to))
        return
    else:
        hanoi(n-1, frm, to, assist)
        res.append((frm, to))
        hanoi(n-1, assist, frm, to)


k = int(input())
res = []
hanoi(k, 1, 2, 3)
print(len(res))
[print(*r) for r in res]