import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
answer = 0
while left <= right: 
    total = 0
    mid = (left+right) // 2
    for i in trees:
        if mid <= i: 
            total += (i-mid)
            if total > M: 
                break
    if total >= M: 
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)