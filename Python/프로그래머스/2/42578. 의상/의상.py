def solution(clothes):
    clothe = {}
    for wear, type in clothes:
        if type not in clothe:
            clothe[type] = 1
        else:
            clothe[type] += 1
    answer = 1
    for i in clothe.values():
        answer *= (i+1)
    return answer-1