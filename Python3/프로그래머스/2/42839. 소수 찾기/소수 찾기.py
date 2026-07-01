import math
from itertools import permutations
def solution(numbers):
    cnt = 0
    lst = set()
    
    for x in range(1, len(numbers)+1):
        for y in permutations(numbers, x):
            lst.add(int(''.join(y)))
    
    for i in lst:
        if is_prime(i):
            cnt += 1
    return cnt

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True