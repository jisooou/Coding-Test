def solution(n, computers):
    visited = [False] * n 
    def dfs(computer):
        visited[computer] = True
        for node in range(n):
            if computers[computer][node] == 1 and not visited[node]:
                dfs(node)
                
    answer = 0
    for computer in range(n):
        if not visited[computer]:
            dfs(computer)
            answer += 1
    return answer