import sys 
from collections import deque
input = sys.stdin.readline

M = int(input())
N = int(input())

graph = [[] for _ in range(M+1)]

for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
queue = deque([1])
visited = [False] * (M+1)
visited[1] = True 
cnt = 0 

while queue: 
    curr_v = queue.popleft()
    for nxt_v in graph[curr_v]:
        if not visited[nxt_v]:
            visited[nxt_v] = True
            queue.append(nxt_v)
            cnt += 1 
print(cnt)