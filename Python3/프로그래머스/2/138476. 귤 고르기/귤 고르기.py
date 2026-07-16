def solution(k, tangerine):
    #서로 다른 종류 최솟값
    collect = {}
    for i in tangerine:
        if i not in collect:
            collect[i] = 1
        else:
            collect[i] += 1   
    sort_collect = sorted(collect.values(), reverse=True)
    
    total = 0
    answer = 0
    for i in sort_collect: 
        total += i 
        answer += 1
        if total >= k:
            return answer
    return answer