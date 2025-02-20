n = int(input()) #입력을 1번만 받기 때문에 sys.stdin.readline().rstrip() 대신 input 사용함.

a, b = 0, 1

for _ in range(n):
	a, b = b, a+b #0과 1 다음 숫자는 (0+1)1, 이때 a가 b가 되므로 그 다음 숫자는 a+b
print(a)