total = 0
num = [int(input()) for _ in range(5)]
num.sort()

for i in num:
	total = total + i
print(total // len(num)) #평균값 

print(num[len(num) // 2]) #중앙값 