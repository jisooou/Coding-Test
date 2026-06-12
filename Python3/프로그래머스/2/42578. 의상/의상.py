def solution(clothes):
    dict = {}
    for name, type in clothes:
        if type not in dict:
            dict[type] = 1
        else:
            dict[type] += 1
    
    answer = 1
    for i in dict.values(): 
        answer *= (i+1)
    return answer-1