def solution(s):
    answer = []
    last = {}
    for i, alpha in enumerate(s): 
        if alpha in last: 
            answer.append(i-last[alpha])
        else: 
            answer.append(-1)
        last[alpha] = i
    return answer