def solution(s):
    stack = []
    for operand in s:
        if operand==')':
            if not stack:
                return False
            if stack[-1] == '(':
                stack.pop()
            else: 
                stack.append(operand)
        else: # '('
            stack.append(operand)
            
    if not stack:
        return True
    else:
        return False