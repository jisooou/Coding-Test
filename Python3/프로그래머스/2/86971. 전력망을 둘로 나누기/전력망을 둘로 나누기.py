from collections import deque
def solution(n, wires):
    answer = n
    for cut_x, cut_y in wires:
        graph = [[] for _ in range(n+1)]
        for a,b in wires:
            if cut_x == a and cut_y == b:
                continue
            graph[a].append(b)
            graph[b].append(a)
            
        queue = deque()
        visited = [False] * (n+1)
        queue.append(1)
        visited[1] = True
        cnt = 1

        while queue:
            current = queue.popleft() 
            for nxt in graph[current]:
                if not visited[nxt]:
                    visited[nxt] = True
                    queue.append(nxt)
                    cnt += 1

        remain = n-cnt
        answer = min(answer, abs(cnt-remain))
    return answer