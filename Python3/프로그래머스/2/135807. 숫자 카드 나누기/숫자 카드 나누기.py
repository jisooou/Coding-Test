import math
def solution(arrayA, arrayB):
    #arrayA 최대공약수 -> arrayB 못 나눔
    #arrayB 최대공약수 -> arrayA 못 나눔
    a_gcd = math.gcd(*arrayA)
    b_gcd = math.gcd(*arrayB)
    answer = 0
    for a in arrayA:
        if a % b_gcd == 0:
            break
    else:
        answer = max(answer, b_gcd)
    
    for b in arrayB:
        if b % a_gcd == 0:
            break
    else:
        answer = max(answer, a_gcd)
            
    return answer