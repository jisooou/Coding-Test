N, C = map(int, input().split())
nums = list(map(int, input().split()))

freq = {}
first = {}

for i in range(N):
    num = nums[i]
    
    if num not in freq: 
        freq[num] = 1
        first[num] = i
    else: 
        freq[num] += 1
        
l = []
for num in freq:
    l.append((-freq[num], first[num], num))
l.sort()
for freq, first, num in l: 
    for _ in range(-freq):
        print(num, end = " ")