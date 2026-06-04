def solution(dirs):
    direction = {
        'U':(0, 1),
        'D':(0, -1),
        'R':(1, 0),
        'L':(-1, 0),
    }
    x, y = 0, 0
    visit = set()
    for d in dirs:
        nx, ny = direction[d]
        dx = nx + x
        dy = ny + y
        if dx<-5 or dx>5 or dy<-5 or dy>5:
            continue
        visit.add((x, y, dx, dy))
        visit.add((dx, dy, x, y))
        x, y = dx, dy
    return len(visit)//2