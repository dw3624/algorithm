import sys
sys.stdin = open('input.txt')


import string
alphabet = string.ascii_lowercase
abc = {}
for i in range(len(alphabet)):
    abc[alphabet[i]] = i+1

L = int(input())
text = input()

ans = 0
for j in range(len(text)):
    ans += (abc[text[j]]) * (31**j)

# print(ans)
print(ans % 1234567891)