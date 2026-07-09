import math
def solution(arrayA, arrayB):
    def get_gcd(arr):
        g = arr[0]
        for num in arr[1:]:
            g = math.gcd(g, num)
        return g
    
    def is_valid(g, arr):
        for i in arr:
            if i % g == 0:
                return False
        return True
        
    a = get_gcd(arrayA)
    b = get_gcd(arrayB)
    
    answer = 0
    
    if is_valid(a, arrayB):
        answer = max(answer, a)
    if is_valid(b, arrayA):
        answer = max(answer, b)
    
    return answer