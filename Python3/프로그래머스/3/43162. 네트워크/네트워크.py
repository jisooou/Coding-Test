# 최단거리를 구하는 문제가 아니다
def solution(n, computers):
    visited = [False] * n 
    def dfs(computer):
        visited[computer] = True
        for node in range(n):
            if computers[computer][node] == 1 and not visited[node]:
                dfs(node)
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer 