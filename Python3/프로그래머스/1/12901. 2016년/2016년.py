date = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def solution(a, b):
    return date[(sum(day[:a-1])+b)%7]