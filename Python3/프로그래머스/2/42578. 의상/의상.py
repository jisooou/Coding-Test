def solution(clothes):
    wear = {}
    for clothe in clothes:
        type = clothe[1]
        if type not in wear:
            wear[type] = 1
        else:
            wear[type] += 1

    answer = 1
    for w in wear.values():      
        answer *= (w+1)
    return answer-1