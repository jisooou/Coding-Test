import math
def solution(brown, yellow):
    collect = []
    box = brown + yellow
    for i in range(1, int(math.sqrt(box))+1):
        if box % i == 0: 
            collect.append(((box//i), i))
    
    for b, y in collect:
        if (b-2)*(y-2) == yellow:
            return [b, y]