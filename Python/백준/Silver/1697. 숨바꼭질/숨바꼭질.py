import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque()
queue.append((N, 0))

MAX = 100000
visited = [False] * (MAX + 1)
visited[N] = True 

while queue: 
    curr_N, cnt = queue.popleft()
    if curr_N == K: 
        print(cnt)
        break 
        
    for nxt_N in (curr_N-1, curr_N+1, curr_N*2):
        if (0 <= nxt_N <= MAX) and not visited[nxt_N]:
            visited[nxt_N] = True
            queue.append((nxt_N, cnt+1))