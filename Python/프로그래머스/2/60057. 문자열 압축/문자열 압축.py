def solution(s):
    answer = len(s)
    for unit in range(1, len(s)//2+1):
        prev = s[0:unit]
        cnt = 1
        compress = ''
        
        for i in range(unit, len(s), unit):
            current = s[i:i+unit]
            
            if prev == current:
                cnt += 1
            else:
                if cnt > 1:
                    compress += str(cnt) + prev
                else: 
                    compress += prev
                prev = current
                cnt = 1
        
        if cnt > 1:
            compress += str(cnt) + prev
        else:
            compress += prev
        answer = min(answer, len(compress))
    return answer
                