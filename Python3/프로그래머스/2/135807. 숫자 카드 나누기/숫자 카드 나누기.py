import math
def solution(arrayA, arrayB):
    #A의 최대공약수 -> B로 안 나눠떨어지는지
    #B의 최대공약수 -> A로 안 나눠떨어지는지
    def get_gcd(array):
        g = array[0]
        for i in array[1:]:
            g = math.gcd(g, i)
        return g
    
    def is_valid(g, array):
        for i in array:
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