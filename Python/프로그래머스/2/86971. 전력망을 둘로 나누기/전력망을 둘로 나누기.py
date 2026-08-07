def solution(n, wires):
    answer = n
    for cut_a, cut_b in wires:
        graph = [[] for _ in range(n+1)]
        for a, b in wires:
            if a == cut_a and b == cut_b:
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
        
        answer_cnt = dfs(1)
        remain = n - answer_cnt
        answer = min(answer, abs(answer_cnt-remain))
    return answer