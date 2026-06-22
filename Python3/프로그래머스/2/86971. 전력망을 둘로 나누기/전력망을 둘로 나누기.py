from collections import deque
def solution(n, wires):
    answer = n
    for remove_a, remove_b in wires:
        graph = [[] for _ in range(n+1)]
        for a, b in wires:
            if remove_a == a and remove_b == b:
                continue
            graph[a].append(b)
            graph[b].append(a)
            
        queue = deque()
        visited = [False] * (n+1)
        queue.append(1)
        visited[1] = True
        cnt = 1
        
        while queue:
            curr_node = queue.popleft()
            for nxt_node in graph[curr_node]:
                if not visited[nxt_node]:
                    visited[nxt_node] = True
                    queue.append(nxt_node)
                    cnt += 1
        rest = n-cnt
        answer = min(answer, abs(cnt-rest))
    return answer