def solution(dirs):
    move = {
        'U':(0,1),
        'D':(0,-1),
        'R':(1,0),
        'L':(-1,0)
    }
    visit = set()
    x, y = 0, 0
    for d in dirs: 
        dx, dy = move[d] #0, 1
        nx = dx + x
        ny = dy + y
        if nx<-5 or nx>5 or ny<-5 or ny>5:
            continue
        visit.add((x, y, nx, ny))
        visit.add((nx, ny, x, y))
        x, y = nx, ny
    return len(visit)//2