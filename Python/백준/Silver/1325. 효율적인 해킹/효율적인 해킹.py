import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[b].append(a)

def bfs(start):
    queue = deque([start])
    visited = [False] * (n+1)
    visited[start] = True 
    cnt = 1
    
    while queue: 
        curr_v = queue.popleft()
        for nxt_v in graph[curr_v]:
            if not visited[nxt_v]:
                visited[nxt_v] = True
                queue.append(nxt_v)
                cnt += 1
    return cnt

max_cnt = 0
result = []
for i in range(1, n+1):
    val = bfs(i)
    if val > max_cnt: #가장 큰 값이 append가 되고
        max_cnt = val 
        result = [i]
    elif val == max_cnt: #그 다음 값이 append가 될 수 있다. 
        result.append(i)
print(*result)        