def solution(k, tangerine):
    tangerine_cnt = {}
    for i in tangerine:
        if i in tangerine_cnt: 
            tangerine_cnt[i] += 1
        else: 
            tangerine_cnt[i] = 1
    counts = sorted(tangerine_cnt.values(), reverse = True)

    answer = 0
    total = 0 
    for c in counts: 
        total += c
        answer += 1
        if total >= k: 
            break
    return answer