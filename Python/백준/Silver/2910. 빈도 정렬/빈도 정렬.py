n, c = map(int, input().split())
nums = list(map(int, input().split()))

freq = {}        
first = {}       

for i in range(n):
    num = nums[i]
    freq[num] = freq.get(num, 0) + 1
    
    if num not in first:
        first[num] = i

v = []

for num in freq:
    v.append((freq[num], num))  

v.sort(key=lambda x: (-x[0], first[x[1]]))

for count, num in v:
    for _ in range(count):
        print(num, end=" ")