def solution(clothes):
    collect = {}
    for i in clothes:
        if i[1] not in collect:
            collect[i[1]] = 1
        else:
            collect[i[1]] += 1
    
    answer = 1
    for i in collect.values():
        answer *= (i+1)
    return answer-1