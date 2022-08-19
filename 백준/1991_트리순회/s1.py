import sys
sys.stdin = open('input.txt')


N = int(input())
nodes = {}
for _ in range(N):
    root, left, right = input().split()
    nodes[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(nodes[root][0])
        preorder(nodes[root][1])

def inorder(root):
    if root != '.':
        inorder(nodes[root][0])
        print(root, end='')
        inorder(nodes[root][1])

def postorder(root):
    if root != '.':
        postorder(nodes[root][0])
        postorder(nodes[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
