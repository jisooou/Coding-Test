# def solution(s):
#     answer = []
#     temp = ""
# #     딕셔너리 이용해서 매핑하기 
#     num_list = {
#         "zero" : "0",
#         "one" : "1",
#         "two" : "2",
#         "three" : "3",
#         "four" : "4",
#         "five" : "5", 
#         "six" : "6",
#         "seven" : "7",
#         "eight" : "8",
#         "nine" : "9"
#     }
# #     문자열을 순회 
#     for i in s: 
#         #i가 영어일 때 - 
#         if i.isalpha():
#             temp = temp + i 
#             if temp in num_list: 
#                 answer.append(num_list[temp])
#                 temp = ""
#         #i가 숫자일 때 
#         elif i.isdigit(): 
#             answer.append(i)
#     return int("".join(answer))

# 다른 답안 
def solution(s):
    num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    answer = s 
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)