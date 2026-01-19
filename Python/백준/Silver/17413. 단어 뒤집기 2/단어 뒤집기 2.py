import sys 
input = sys.stdin.readline 

S = input().rstrip()

answer = []
stack = []
i = 0
n = len(S)

while i < n: 
    # < 인 경우 
    if S[i] == '<': 
        while stack:
            answer.append(stack.pop())
        # > 가 나오기 전까지 
        while i < n and S[i] != '>':
            answer.append(S[i])
            i += 1 
        # > 가 나오면 
        answer.append('>')
        i += 1 
        
    # 공백인 경우 
    elif S[i] == ' ':
        while stack: 
            answer.append(stack.pop())
        answer.append(' ')
        i += 1
        
    # 일반 문자인 경우 
    else: 
        stack.append(S[i])
        i += 1 
        
while stack: 
    answer.append(stack.pop())

print(''.join(answer))