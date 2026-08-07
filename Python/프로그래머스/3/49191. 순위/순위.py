from collections import deque
def solution(n, results):
    win_graph = [[] for _ in range(n+1)]
    loose_graph = [[] for _ in range(n+1)]
    for a, b in results:
        win_graph[a].append(b)
        loose_graph[b].append(a)
    
    def dfs(player, graph):
        queue = deque()
        queue.append(player)
        visited = [False] * (n+1)
        cnt = 0
        while queue:
            current = queue.popleft()
            for nxt in graph[current]:
                if not visited[nxt]:
                    visited[nxt] = True
                    queue.append(nxt)
                    cnt += 1
        return cnt 
    
    answer = 0
    for i in range(1, n+1):
        win_player = dfs(i, win_graph)
        loose_player = dfs(i, loose_graph)
        if win_player + loose_player == n-1:
            answer += 1
    return answer