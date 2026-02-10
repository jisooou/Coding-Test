import sys
input = sys.stdin.readline

N = int(input())
budget = list(map(int, input().split()))
M = int(input())

left = 0
right = max(budget)
answer = 0
while left <= right:
    total = 0
    mid = (left + right) // 2
    for i in budget: 
        total += min(i, mid)
    if total <= M: 
        answer = mid
        left = mid + 1
    else: 
        right = mid - 1
print(answer)