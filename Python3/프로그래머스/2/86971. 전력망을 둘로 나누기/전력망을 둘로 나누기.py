def solution(n, wires):
    #하나를 끊어서 개수 비슷하게->개수 차이(절대값)
    answer = n
    for cut_a, cut_b in wires:
        graph = [[] for _ in range(n+1)]
        for a, b in wires:
            if cut_a == a and cut_b == b:
                continue
            graph[a].append(b) 
            graph[b].append(a)
        
        visited = [False] * (n+1)
        def dfs(current):
            visited[current] = True
            cnt = 1
            for nxt in graph[current]:
                if not visited[nxt]:
                    cnt += dfs(nxt)
            return cnt
        
        count = dfs(1)
        remain = n - count
        answer = min(answer, abs(count-remain))
    return answer