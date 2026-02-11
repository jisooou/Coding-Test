import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

#BFS : 큐를 사용 
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [-1] * (N+1)
queue = deque([X])
dist[X] = 0

while queue: 
    curr_n = queue.popleft()
    for nxt_n in graph[curr_n]:
        if (dist[nxt_n] == -1):
            dist[nxt_n] = dist[curr_n] + 1
            queue.append(nxt_n)
found = False
for i in range(1, N+1):
    if dist[i] == K: 
        print(i)
        found = True
if not found: 
    print(-1)
        