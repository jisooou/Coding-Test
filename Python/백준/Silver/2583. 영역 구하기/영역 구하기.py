from collections import deque
m, n, k = map(int, input().split())
dist = [[0]*n for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            dist[y][x] = 1

def bfs(row, col):
    queue = deque()
    queue.append((row, col))
    dist[row][col] = 1
    area = 1 
    
    while queue: 
        x, y = queue.popleft()
        for i in range(4):
            rx = dx[i] + x
            cy = dy[i] + y
        
            if 0 <= rx < m and 0 <= cy < n and dist[rx][cy] == 0: 
                dist[rx][cy] = 1
                queue.append((rx, cy))
                area += 1 #1로 채워진 area
    return area

answer = []
for i in range(m):
    for j in range(n):
        if dist[i][j] == 0: 
            answer.append(bfs(i, j))
answer.sort()

print(len(answer))
print(*answer)