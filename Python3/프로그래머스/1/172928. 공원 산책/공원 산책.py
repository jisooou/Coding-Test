def solution(park, routes):
    direct_dict = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    row = len(park)
    column = len(park[0])
    x, y = 0, 0
    for i in range(row):
        for j in range(column):
            if park[i][j]=='S':
                x, y = i, j
                
    for r in routes:
        direct, cnt = r.split()
        cnt = int(cnt)
        can_move = True
        dx, dy =  direct_dict[direct]
        nx, ny = x, y
        for _ in range(cnt):
            nx += dx
            ny += dy
            if nx<0 or nx>=row or ny<0 or ny>=column or park[nx][ny]=='X':
                can_move = False
                break
        if can_move: 
            x, y = nx, ny
    return [x, y]