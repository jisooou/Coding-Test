def solution(t, p):
#    문자열 다루는 문제
    n = len(p)
    cnt = 0
    for i in range(len(t)-len(p)+1):
        slice = t[i:i+n]
        if int(slice) <= int(p):
            cnt += 1
    return cnt