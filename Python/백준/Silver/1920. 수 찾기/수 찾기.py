import sys

N = int(sys.stdin.readline().rstrip())
a = set(map(int, sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().rstrip().split()))

for i in b:
	if i in a:
		print(1)
	else:
		print(0)