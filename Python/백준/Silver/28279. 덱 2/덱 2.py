import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())

d = deque()

for _ in range(N): 
	num = list(map(int, sys.stdin.readline().rstrip().split()))
	if num[0] == 1:
		d.appendleft(num[1])
	elif num[0] == 2:
		d.append(num[1])
	elif num[0] == 3: 
		print(d.popleft() if d else -1)
	elif num[0] == 4:
		print(d.pop() if d else -1)
	elif num[0] == 5:
		print(len(d))
	elif num[0] == 6:
		print(0 if d else 1)
	elif num[0] == 7:
		print(d[0] if d else -1)
	elif num[0] == 8:
		print(d[-1] if d else -1)