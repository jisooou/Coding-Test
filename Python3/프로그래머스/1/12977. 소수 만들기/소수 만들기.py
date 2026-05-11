# 소수 판별법
from itertools import combinations
import math
def solution(nums):
    cnt = 0
    for comb in combinations(nums, 3):
        total = sum(comb)
        is_prime = True 
        for i in range(2, int(math.sqrt(total))+1):
            if total % i == 0:
                is_prime = False
                break
        if is_prime:
            cnt += 1  
    return cnt