import sys

def count_long_stick(heights):
	stack = []
	cnt = 0 
	for h in reversed(heights):
		if not stack or h > stack[-1]:
			cnt = cnt + 1
			stack.append(h)
	return cnt

input = sys.stdin.readline
N = int(input())
heights = [int(input()) for _ in range(N)]
print(count_long_stick(heights))