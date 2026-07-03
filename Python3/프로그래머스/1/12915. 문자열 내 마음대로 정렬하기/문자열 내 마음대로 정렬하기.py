def solution(strings, n):
    strings.sort() 
    lst = sorted(strings, key=lambda x: x[n])
    return lst
        