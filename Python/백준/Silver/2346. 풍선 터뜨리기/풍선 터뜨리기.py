import sys
from collections import deque 

input = sys.stdin.readline
ans_list = []
N = int(input()) #5 
nums = list(map(int, input().split()))
q = deque((i+1, nums[i]) for i in range(N))
while q: 
    index, move = q.popleft()
    ans_list.append(index)
    if not q: 
        break
    else: 
        if move > 0: 
            q.rotate(-(move-1))
        else: 
            q.rotate(-move)
print(*ans_list)
        
    