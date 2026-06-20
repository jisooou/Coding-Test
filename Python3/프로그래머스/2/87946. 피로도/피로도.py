from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for permute in permutations(dungeons):
        fatigue = k
        cnt = 0
        for x, y in permute:
            if fatigue >= x:
                fatigue -= y
                cnt += 1
        answer = max(answer, cnt)
    return answer