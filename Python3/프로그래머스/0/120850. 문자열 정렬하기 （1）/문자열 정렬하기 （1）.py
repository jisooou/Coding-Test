def solution(my_string):
    answer = []
    for num in my_string:
        if num.isdigit():
            answer.append(num)
    answer.sort()
    return list(map(int, answer))