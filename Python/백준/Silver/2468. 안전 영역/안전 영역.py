from collections import deque
N = int(input())

dist = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, h):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True 
    while queue: 
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and dist[nx][ny] > h:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
max_h = max(map(max, dist))
answer = 0 

for h in range(max_h+1): 
    visited = [[False]*N for _ in range(N)]
    cnt = 0 
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and dist[i][j] > h: 
                bfs(i, j, h)
                cnt += 1
    answer = max(answer, cnt)
print(answer)