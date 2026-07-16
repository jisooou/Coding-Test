def solution(k, dungeons):
    visited = [False] * len(dungeons)
    answer = 0
    def dfs(current, cnt):
        nonlocal answer
        answer = max(answer, cnt)
        for i in range(len(dungeons)): 
            need = dungeons[i][0]
            used = dungeons[i][1]
            if not visited[i] and current >= need:
                visited[i] = True
                dfs(current-used, cnt+1)
                visited[i] = False
    dfs(k, 0)
    return answer