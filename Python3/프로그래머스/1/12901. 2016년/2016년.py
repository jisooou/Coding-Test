def solution(a, b):
    #1월1일 금요일
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    month_sum = 0
    for i in range(a-1):
        month_sum += month[i]
    calen = month_sum + b - 1
    return day[calen%len(day)]