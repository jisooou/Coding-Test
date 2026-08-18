import math
def solution(n, k):
    result = []
    numbers = [i for i in range(1, n+1)]
    k = k - 1
    while numbers: 
        block = math.factorial(len(numbers)-1)
        idx = k // block
        result.append(numbers.pop(idx))
        
        k = k % block
    return result