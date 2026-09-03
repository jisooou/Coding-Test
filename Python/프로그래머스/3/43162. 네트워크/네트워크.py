def solution(n, computers):
    visited = [False]*n
    answer = 0
    
    def dfs(current):
        visited[current] = True
        for nxt in range(n):
            if computers[current][nxt] and not visited[nxt]:
                dfs(nxt)
                    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer