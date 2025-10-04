#ord() 숫자로, chd() 알파벳으로
def solution(s, n):
    result = []
    #s를 어떻게 자를 것인가? 
    for i in s: 
#         전부 대문자일 경우 
        if i.isupper():
            #A: 65, B: 66 / z -> a
            result.append(chr(((ord(i)-ord('A')+n) % 26) + ord('A')))
#             전부 소문자일 경우
        elif i.islower(): 
            result.append(chr(((ord(i)-ord('a')+n) % 26) + ord('a')))
#             공백일 경우
        else: 
            result.append(i)
    return("".join(result))
            