import math
def solution(number, limit, power):
    num_cnt = []
    for num in range(1, number+1): 
        cnt = 0
        for i in range(1, int(math.sqrt(num))+1): 
            if num % i == 0:
                if i * i == num:
                    cnt += 1
                else:
                    cnt += 2
        num_cnt.append(cnt)
    
    total = 0
    for n in num_cnt:
        if n > limit:
            total += power
        else:
            total += n  
    return total