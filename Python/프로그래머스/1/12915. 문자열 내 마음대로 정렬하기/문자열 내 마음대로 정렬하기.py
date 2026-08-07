def solution(strings, n):
    sort_strings = sorted(strings, key=lambda x: (x[n], x))
    return sort_strings