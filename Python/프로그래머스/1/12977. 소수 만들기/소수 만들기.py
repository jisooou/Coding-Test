from itertools import combinations
import math
def solution(nums):
    answer = 0
    for num in combinations(nums, 3):
        total = sum(num)
        is_prime = True
        for i in range(2, int(math.sqrt(total))+1):
            if total%2==0 or total%i==0:
                is_prime = False
        if is_prime:
            answer += 1

    return answer