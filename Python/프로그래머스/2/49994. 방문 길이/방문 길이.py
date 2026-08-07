def solution(dirs):
    direct = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }
    cx, cy = 0, 0
    result = set()
    for d in dirs: 
        dx, dy = direct[d]
        nx = cx + dx
        ny = cy + dy
        if nx>5 or nx<-5 or ny>5 or ny<-5:
            continue
        result.add((cx, cy, nx, ny))
        result.add((nx, ny, cx, cy))
        cx, cy = nx, ny
    return len(result)//2