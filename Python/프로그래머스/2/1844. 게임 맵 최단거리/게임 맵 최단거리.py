from collections import deque
def solution(maps):
    row = len(maps)
    column = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx<0 or nx>=row or ny<0 or ny>=column:
                continue
            if maps[nx][ny] == 0:
                continue
                
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[cx][cy] + 1
                queue.append((nx, ny))
                
    if maps[row-1][column-1] == 1:
        return -1
    return maps[row-1][column-1]
                