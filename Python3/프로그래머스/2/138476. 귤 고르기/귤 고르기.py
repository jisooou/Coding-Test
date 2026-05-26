from collections import Counter
def solution(k, tangerine):
    tang_dict = Counter(tangerine)
    total = 0
    answer = 0
    tang_cnt = sorted(tang_dict.values(), reverse=True)
    for c in tang_cnt:
        total += c
        answer += 1
        if total >= k:
            return answer
            