import sys
sys.stdin = open('input.txt')

n = int(input())
# s = [0, 1, 2]
# for i in range(3, n+1):
#     s.append(s[i-2] + s[i-1])
# print(s[n] % 10007)

s = [0] * 1001
s[1] = 1
s[2] = 2
for i in range(3, n+1):
    s[i] = s[i-1] + s[i-2]
print(s[n]%10007)
