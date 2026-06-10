from collections import deque
def solution(n, computers):
    visited = [False] * n
    answer = 0 
    for node in range(n):
        if not visited[node]:
            answer += 1
            
            queue = deque()
            queue.append(node)
            while queue:
                current_node = queue.popleft()
                for connect_node in range(n):
                    if not visited[connect_node] and computers[current_node][connect_node] == 1:
                        visited[connect_node] = True
                        queue.append(connect_node)
    return answer