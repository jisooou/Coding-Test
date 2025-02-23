n = int(input())

start = 0
end = n

while start <= end: 
	mid = (start + end) // 2 
	
	if mid ** 2 < n: #중앙값의 제곱근이 n보다 작은 경우, 중앙값을 더 큰 값으로 잡는다. 
			start = mid + 1
	else: #중앙값의 제곱근이 n보다 클 경우, 중앙값을 더 작은 값으로 잡는다.
			end = mid - 1

print(start)