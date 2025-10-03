def solution(phone_number):
    phone_number_star = "*" * len(phone_number[:-4]) #0103333 -> *******
    answer = phone_number_star + phone_number[-4:]
    return answer