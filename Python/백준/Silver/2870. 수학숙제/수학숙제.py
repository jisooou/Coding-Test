N = int(input())

temp = ""
answer = []

for _ in range(N):
    word = input().strip()
    for ch in word: 
        if ch.isdigit():
            temp += ch 
        else: #문자인 경우 
            if temp != "":
                answer.append(int(temp))
                temp = ""
    if temp != "":            
        answer.append(int(temp))
        temp = ""
answer.sort()
for i in answer: 
    print(i) 