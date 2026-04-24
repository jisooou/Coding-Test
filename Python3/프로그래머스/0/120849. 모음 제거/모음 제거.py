def solution(my_string):
    answer = ''
    vowel = ['a', 'e', 'i', 'o', 'u']
    for w in my_string: 
        if w not in vowel: 
            answer += w
    return answer