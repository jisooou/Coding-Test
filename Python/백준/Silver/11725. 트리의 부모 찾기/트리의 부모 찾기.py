import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)] #1부터 7까지 나타내야 하니까 (7+1까지)

for _ in range(N-1): #0 1 2 3 4 5 (N-1까지)
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (N+1)
visited[1] = True
parent = [0] * (N+1)

def dfs(curr_v):
    for nxt_v in graph[curr_v]:
        if not visited[nxt_v]:
            visited[nxt_v] = True
            parent[nxt_v] = curr_v
            dfs(nxt_v)
    
dfs(1)
for i in range(2, N+1):
    print(parent[i])