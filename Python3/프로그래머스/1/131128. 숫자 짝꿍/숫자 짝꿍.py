from collections import Counter
def solution(X, Y):
    answer = ''
    x_counter = Counter(X)
    y_counter = Counter(Y)
    
    for num in range(9, -1, -1):
        num = str(num)
        common = min(x_counter[num], y_counter[num])
        answer += common * num
    
    if answer == '':
        return '-1'
    if answer[0] == '0':
        return '0'
    return answer