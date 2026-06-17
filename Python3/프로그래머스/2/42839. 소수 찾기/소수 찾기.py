import math
from itertools import permutations

def is_prime(num):
    if num < 2: 
        return False
    
    for j in range(2, int(math.sqrt(num))+1):
        if num % j == 0:
            return False
    return True
    
def solution(numbers):
    permu_set = set()
    for length in range(1, len(numbers)+1):
        for p in permutations(numbers, length):
            permu_set.add(int(''.join(p)))
    
    cnt = 0
    for i in permu_set:
        if is_prime(i):
            cnt += 1
    return cnt