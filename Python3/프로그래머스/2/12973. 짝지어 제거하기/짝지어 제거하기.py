def solution(s):
    #다없어지면 1, 아니면 0 
    stack = []
    for word in s:
        if not stack:
            stack.append(word)
        else: 
            if stack and stack[-1]==word:
                stack.pop()
            else:
                stack.append(word)
    
    if not stack:
        return 1
    else:
        return 0