import math
from itertools import permutations
            
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True
    
def solution(numbers):
    cnt = 0
    get_set = set()
    for length in range(1, len(numbers)+1):
        for i in permutations(numbers, length): 
            get_set.add(int(''.join(i)))
            
    for p in get_set:
        if is_prime(p):
            cnt += 1
    return cnt 