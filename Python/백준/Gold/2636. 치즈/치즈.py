from collections import deque

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
time_cnt = 0
last_cnt = 0

while True:    
    cheese_cnt = 0
    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 1:
                cheese_cnt += 1
    # 치즈가 다 녹고 없는 경우
    if cheese_cnt == 0: 
        break
    last_cnt = cheese_cnt
    
    visited = [[False]*M for _ in range(N)]
    visited[0][0] = True
    
    queue = deque()
    queue.append((0, 0))
    
    melt = []
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if cheese[nx][ny] == 1:
                    visited[nx][ny] = True
                    melt.append((nx, ny))
                elif cheese[nx][ny] == 0: 
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                  
                
    for x, y in melt: 
        cheese[x][y] = 0
    time_cnt += 1
print(time_cnt)
print(last_cnt)