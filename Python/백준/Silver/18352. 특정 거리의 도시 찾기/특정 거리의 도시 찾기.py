import sys
import heapq
input = sys.stdin.readline
INF = int(1e9) # 무한대

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [INF] * (N+1)
dist[X] = 0

heap = []
heapq.heappush(heap, (0, X))

while heap: 
    curr_dist, curr_v = heapq.heappop(heap)
    if curr_dist > dist[curr_v]:
        continue
        
    for nxt_v in graph[curr_v]:
        new_dist = curr_dist + 1 # 1이 추가
        if new_dist < dist[nxt_v]:
            dist[nxt_v] = new_dist
            heapq.heappush(heap, (new_dist, nxt_v))
            
found = False
for i in range(1, N+1):
    if dist[i] == K: 
        print(i)
        found = True
if not found:
    print(-1)