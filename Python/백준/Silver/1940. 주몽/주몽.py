import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
nums = sorted(map(int, input().split()))

left = 0 
right = N-1
cnt = 0

while left < right: 
    total = nums[left] + nums[right]
    if total == M: 
        cnt += 1
        left += 1
        right -= 1
    elif total < M: 
        left += 1
    elif total > M: 
        right -= 1
print(cnt)  