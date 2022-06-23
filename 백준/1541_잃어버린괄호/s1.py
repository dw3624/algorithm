import sys
sys.stdin = open('input.txt')

line = input().split('-')

val = sum(map(int, line[0].split('+')))
for l in line[1:]:
    n = sum(map(int, l.split('+')))
    val -= n

print(val)