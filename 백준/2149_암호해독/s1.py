import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


keys = input().strip()
sentence = input().strip()

i_keys = []
for i in range(len(keys)):
    i_keys.append((i, keys[i]))
i_keys.sort(key=lambda x: (x[1], x[0]))

pwds = ['' for _ in range(len(sentence) // len(keys))]
for i in range(len(sentence)):
    pwds[i % (len(sentence) // len(keys))] += sentence[i]

ans = ''
for pwd in pwds:
    tmp = [0] * len(pwd)
    for org_i in range(len(pwd)):
        new_i = i_keys[org_i][0]
        tmp[new_i] = pwd[org_i]
    for t in tmp:
        ans += t

print(ans)

