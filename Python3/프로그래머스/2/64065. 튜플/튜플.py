def solution(s):
    collect = {}
    s = s.replace('{', '')
    s = s.replace('}', '')
    nums = s.split(',')
    for i in nums:
        if i not in collect:
            collect[i] = 1
        else:
            collect[i] +=1

    answer = []
    sort_collect = sorted(collect.items(), key=lambda x: x[1], reverse=True)
    for pair in sort_collect:
        answer.append(int(pair[0]))
    return answer
        
        
        