import sys
input = sys.stdin.readline

N = int(input()) #4
budget = list(map(int, input().split()))
M = int(input()) #485

left = 0
right = max(budget)
answer = 0

#left와 right를 움직여야 함
while left <= right: 
    mid = (left + right) // 2
    sum = 0
    for i in budget: 
        sum += min(i, mid)
    if sum <= M:
        answer = mid
        left = mid + 1
    else: 
        right = mid - 1
print(answer)        