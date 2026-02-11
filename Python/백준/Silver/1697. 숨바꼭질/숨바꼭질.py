import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

MAX = 100000
visited = [False] * (MAX+1)
visited[N] = True

queue = deque()
queue.append((N, 0))

while queue: 
    curr_v, cnt = queue.popleft()
    if curr_v == K: 
        print(cnt)
        break 
    for nxt_v in (curr_v-1, curr_v+1, curr_v*2):
        if (0 <= nxt_v <= MAX) and not visited[nxt_v]:
            visited[nxt_v] = True
            queue.append((nxt_v, cnt+1))