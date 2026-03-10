from collections import deque
M, N, K = map(int, input().split())
dist = [[0]*N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            dist[y][x] = 1

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    dist[r][c] = 1
    area = 1 
    while queue: 
        row, col = queue.popleft()
        for i in range(4):
            nr = row + dx[i]
            nc = col + dy[i]
            if 0 <= nr < M and 0 <= nc < N and dist[nr][nc] == 0: 
                dist[nr][nc] = 1
                queue.append((nr, nc))
                area += 1 
    return area
answer = []
for i in range(M):
    for j in range(N):
        if dist[i][j] == 0: 
            answer.append(bfs(i,j))
answer.sort()  
print(len(answer))
print(*answer)