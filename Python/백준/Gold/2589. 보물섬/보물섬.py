import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
treasure = [input().strip() for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

def bfs(cx, cy): 
    queue = deque()
    queue.append((cx, cy))
            
    dist = [[-1] * m for _ in range(n)]
    dist[cx][cy] = 0
            
    max_dist = 0
    
    while queue: 
        x, y = queue.popleft()
        for move in range(4):
            nx = dx[move] + x
            ny = dy[move] + y
            if 0 <= nx < n and 0 <= ny < m:
                if treasure[nx][ny] == 'L' and dist[nx][ny] == -1:  
                    queue.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
                    max_dist = max(max_dist, dist[nx][ny])
    return max_dist    

answer = 0                            
for i in range(n):
    for j in range(m):
        if treasure[i][j] == 'L':
            answer = max(answer, bfs(i, j))
print(answer)