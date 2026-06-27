def solution(s):
    answer = []
    s = s.replace('{', '')
    s = s.replace('}', '')
    s = s.split(',')
    collect = {}
    for i in s:
        if i not in collect:
            collect[i] = 1
        else:
            collect[i] += 1
    
    sorted_collect = sorted(collect.items(), key=lambda x: x[1], reverse=True)
    for i in sorted_collect:
        answer.append(int(i[0]))
    return answer
    