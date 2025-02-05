import sys

sum = 0

X = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    sum = sum + (a * b) 

if(sum == X):
	print("Yes")
else:
	print("No")