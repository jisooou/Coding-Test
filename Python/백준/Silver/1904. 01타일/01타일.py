N = int(input())
a, b = 1, 2

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
	for _ in range(3, N + 1):
		a, b = b, (a + b) % 15746
	print(b)