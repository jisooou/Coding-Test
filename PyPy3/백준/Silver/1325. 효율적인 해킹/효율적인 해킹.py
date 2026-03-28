from collections import deque
import sys

input = sys.stdin.readline 
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    visited = [False] * (n+1)
    queue = deque([start])
    visited[start] = True
    cnt = 1
    while queue: 
        now = queue.popleft()
        for nxt in graph[now]: 
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)
                cnt += 1
    return cnt             

# 최대 값을 찾기 위해 
max_val = 0 
result = []

for i in range(1, n+1):
    val = bfs(i)
    if val > max_val: 
        max_val = val 
        result = [i]
    elif val == max_val: 
        result.append(i)
print(*result)