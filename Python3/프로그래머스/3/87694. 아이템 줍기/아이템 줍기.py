from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((characterX, characterY, 0))
    
    box = [[0]*102 for _ in range(102)] 
    box[characterY][characterX] = 0
    
    for startX, startY, endX, endY in rectangle:
        startX *= 2
        startY *= 2
        endX *= 2
        endY *= 2
        for i in range(startX, endX+1):
            for j in range(startY, endY+1):
                box[j][i] = 1
                
    for startX, startY, endX, endY in rectangle:
        startX *= 2
        startY *= 2
        endX *= 2
        endY *= 2
        for i in range(startX+1, endX):
            for j in range(startY+1, endY):
                box[j][i] = 0
    while queue:
        currentX, currentY, cnt = queue.popleft()
        if currentX==itemX and currentY==itemY: 
            return cnt//2
        for i in range(4):
            nextX = currentX + dx[i]
            nextY = currentY + dy[i]
            if box[nextY][nextX] == 1:
                box[nextY][nextX] = 0
                queue.append((nextX, nextY, cnt+1))