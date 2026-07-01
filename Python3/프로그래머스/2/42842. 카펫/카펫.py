import math
def solution(brown, yellow):
    #규칙을 찾는다 
    answer = []
    carpet = brown + yellow
    for h in range(1, int(math.sqrt(carpet))+1):
        if carpet % h == 0:
            w = carpet // h
        if (w-2)*(h-2) == yellow:
            if w >= h:
                answer.append(w)
                answer.append(h)
    return answer     