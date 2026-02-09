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
        if i > mid: 
            total += (i-mid)
            if total > M: # 시간 초과 방지
                break 
    if total >= M: # 나무 높이 기준선을 너무 낮게 잡은 것
        answer = mid
        left = mid + 1
    else: # 나무 높이 기준선을 너무 높게 잡은 것  
        right = mid - 1
print(answer)