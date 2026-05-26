#종류가 최소가 되도록
def solution(k, tangerine):
    tang_dict = {}
    for t in tangerine:
        if t not in tang_dict:
            tang_dict[t] = 1
        else:
            tang_dict[t] += 1
    total = 0
    answer = 0
    tang_cnt = sorted(tang_dict.values(), reverse=True)
    for c in tang_cnt:
        total += c
        answer += 1
        if total >= k:
            return answer
            