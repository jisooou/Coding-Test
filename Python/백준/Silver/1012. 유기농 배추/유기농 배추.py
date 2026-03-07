from collections import deque
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1
        
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(cabb_x, cabb_y):
        queue = deque()
        queue.append((cabb_x, cabb_y))
        graph[cabb_x][cabb_y] = 0
    
        while queue: 
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
            
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)