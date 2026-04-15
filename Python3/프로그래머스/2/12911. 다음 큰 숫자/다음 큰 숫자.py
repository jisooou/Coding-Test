#2진수를 변환해 주는 함수 - bin()
def solution(n):
    cnt_n = bin(n)[2:].count('1')
    while True: 
        n += 1
        if cnt_n == bin(n)[2:].count('1'):
            break 
    return n