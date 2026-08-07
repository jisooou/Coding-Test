def solution(n):
    num_string = ''
    while n != 0:
        num_string += str(n%3)
        n //= 3
    return int(num_string, 3)