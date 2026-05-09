def solution(n, m, section):
    cnt = 0
    last_painted = 0
    for s in section: 
        if s > last_painted:
            last_painted = s + m - 1
            cnt += 1
    return cnt