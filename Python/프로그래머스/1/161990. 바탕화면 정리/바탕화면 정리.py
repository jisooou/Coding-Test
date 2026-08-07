#사각형을 찾는 문제
def solution(wallpaper):
    min_row = len(wallpaper)
    min_column = len(wallpaper[0])
    max_row = 0
    max_column = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                min_row = min(min_row, i)
                min_column = min(min_column, j)
                max_row = max(max_row, i)
                max_column = max(max_column, j)
    return [min_row, min_column, max_row+1, max_column+1]
    