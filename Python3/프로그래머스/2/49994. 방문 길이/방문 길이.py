def solution(dirs):
    direct = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }
    currentX, currentY = 0, 0
    visited = set()
    for dir in dirs:
        nxtX, nxtY = direct[dir]
        newX = nxtX + currentX
        newY = nxtY + currentY
        if newX>5 or newX<-5 or newY>5 or newY<-5:
            continue
        visited.add((currentX, currentY, newX, newY))
        visited.add((newX, newY, currentX, currentY))
        currentX, currentY = newX, newY
    return len(visited)//2