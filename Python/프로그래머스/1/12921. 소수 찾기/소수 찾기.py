# 에라토스테네스의 체 알고리즘 
import math

def solution(n):
    is_prime = [True] * (n+1)
    is_prime[0], is_prime[1] = False, False
    
    for i in range(2, int(math.sqrt(n)+1)):
        if is_prime[i]: #2,3
            for j in range(i*i, n+1, i):
                is_prime[j] = False
                
    cnt = 0 
    for num in range(2, n+1):
        if is_prime[num]:
            cnt += 1
            
    return cnt 