def solution(n):
    answer = ''
    while n > 0:
        remain = str(n % 3)
        if remain == '1':
            answer = '1' + answer
            n //= 3
        elif remain == '2':
            answer = '2' + answer
            n //= 3
        elif remain == '0':
            answer = '4' + answer
            n = n // 3 - 1
    return answer