from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    distance = [-1]*(n+1)
    distance[1] = 0
    queue = deque()
    queue.append(1)
    while queue:
        current = queue.popleft()
        for nxt in graph[current]:
            if distance[nxt] == -1:
                distance[nxt] = distance[current]+1
                queue.append(nxt)
    max_distance = max(distance)
    return distance.count(max_distance)