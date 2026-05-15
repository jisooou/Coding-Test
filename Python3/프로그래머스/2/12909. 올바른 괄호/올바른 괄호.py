def solution(s):
    stack = []
    for operand in s:
        if operand == '(':
            stack.append(operand)
        else: # ')'
            if not stack:
                return False
            stack.pop()
    return not stack