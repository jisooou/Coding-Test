import sys

total = 0 
n = int(sys.stdin.readline().rstrip())

for i in range(1, n+1): 
	total = total + i
	
print(total)