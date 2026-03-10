from collections import deque
T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    dist = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        dist[b][a] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
        
    def bfs(ax, ay):
        queue = deque()
        queue.append((ax, ay))
        dist[ax][ay] = 0 
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == 1: 
                    dist[nx][ny] = 0 
                    queue.append((nx, ny))
    cnt = 0 
    for i in range(n):
        for j in range(m):
            if dist[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)           