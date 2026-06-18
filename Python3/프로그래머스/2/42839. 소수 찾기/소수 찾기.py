from itertools import permutations
import math

def is_prime(num):
    if num < 2: 
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(numbers): 
    collect = set()
    for length in range(1, len(numbers)+1):
        for i in permutations(numbers, length): 
            collect.add(int(''.join(i)))
    
    cnt = 0
    for j in collect:
        if is_prime(j):
            cnt += 1
    return cnt