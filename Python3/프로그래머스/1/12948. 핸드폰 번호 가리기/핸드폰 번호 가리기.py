def solution(phone_number):
    star_count = len(phone_number)-4 #맨 뒤 4자리는 제외 
    star_phone_number = "*" * star_count
    answer = star_phone_number + phone_number[-4:]
    return answer