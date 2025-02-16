import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())

queue = deque()

for _ in range(N): 
	x = sys.stdin.readline().rstrip().split()
	if x[0] == 'push':
		queue.append(x[1])
	elif x[0] == 'pop': 
		if len(queue) > 0:
			print(queue.popleft())
		else: 
			print(-1)
	elif x[0] == 'size':
		print(len(queue))
	elif x[0] == 'empty':
		if len(queue) == 0: 
			print(1)
		else:
			print(0)
	elif x[0] == 'front':
		if len(queue) > 0:
			print(queue[0])
		else:
			print(-1)
	elif x[0] == 'back':
		if len(queue) > 0:
			print(queue[-1])
		else:
			print(-1)