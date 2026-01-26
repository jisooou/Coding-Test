import sys
from collections import deque
input = sys.stdin.readline

M = int(input())
N = int(input())

graph = [[] for _ in range(M+1)] # index 0은 처리 X

for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
queue = deque([1])
visited = [False] * (M+1)
visited[1] = True 
cnt = 0 

while queue: 
    cur_v = queue.popleft()
    for next_v in graph[cur_v]:
        if not visited[next_v]:
            visited[next_v] = True
            queue.append(next_v)
            cnt += 1
print(cnt)