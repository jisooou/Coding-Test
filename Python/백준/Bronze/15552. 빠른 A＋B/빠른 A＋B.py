import sys

num = sys.stdin.readline().rstrip()
num = int(num)
for _ in range(num):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)
    