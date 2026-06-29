def solution(s):
    transform = 0
    zero_cnt = 0
    while s != '1':
        origin_s = len(s)
        s = s.replace('0', '')
        replace_s = len(s)
        zero_cnt += origin_s - replace_s
    
        s = bin(len(s))[2:]
        transform += 1
    return [transform, zero_cnt]