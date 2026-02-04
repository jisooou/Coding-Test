import sys
from collections import deque
#런타임 에러 해결 > DFS 재귀호출 제한을 둬야한다
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    # [1: 6 4][2: 4] [3: 5] [4: 1 2] [5: 3] [6: 3] [7: 4]

visited = [False] * (N+1)
visited[1] = True
parent = [0] * (N+1)
# curr_v 방문 -> nxt_v 새로 방문했으면 = curr_v가 nxt_v의 부모 노드
def dfs(curr_v):
    for nxt_v in graph[curr_v]:
        if not visited[nxt_v]:
            visited[nxt_v] = True
            parent[nxt_v] = curr_v
            dfs(nxt_v)
    
dfs(1)
for i in range(2, N+1):
    print(parent[i])