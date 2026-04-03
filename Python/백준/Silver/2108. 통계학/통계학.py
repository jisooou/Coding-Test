import sys
input = sys.stdin.readline

n = int(input())
aver = 0
mid = 0
freq = 0
rang = 0

total = 0
arr = []
freq_cnt = {}
for _ in range(n):
    num = int(input())
    total += num 
    arr.append(num)
    
    if num in freq_cnt: 
        freq_cnt[num] += 1
    else: 
        freq_cnt[num] = 1
    
arr.sort()    

# 1. 산술평균
if total >= 0: 
    aver = int((total / n) + 0.5)
else: 
    aver = int((total / n) - 0.5)
    
# 2. 중앙값
mid = arr[n // 2]

# 3. 최빈값
max_freq = max(freq_cnt.values())
possi_value = []
for key in freq_cnt: 
    if freq_cnt[key] == max_freq: 
        possi_value.append(key)
possi_value.sort()    
if len(possi_value) > 1: 
    freq = possi_value[1]
else: 
    freq = possi_value[0]
        
# 4. 범위
rang = arr[n-1] - arr[0]

print(aver)
print(mid)
print(freq)
print(rang)