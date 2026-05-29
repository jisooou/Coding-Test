def solution(n, m, section):
    cnt = 0
    paint = 0
    for s in section: 
        if paint < s:
            paint = s + m - 1
            cnt += 1
    return cnt