def solution(s):
    answer = 0
    same = 0
    diff = 0
    before_w = ''
    for char in s:
        if same == 0:
            same = 1
            before_w = char
        elif char == before_w:
            same += 1
        else:
            diff += 1
        
        if same == diff:
            answer += 1
            same = 0
            diff = 0
    if same != 0:
        answer += 1
    return answer