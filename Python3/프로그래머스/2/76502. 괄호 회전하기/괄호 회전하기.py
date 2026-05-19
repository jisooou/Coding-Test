def is_valid(rotate):
    stack = []
    pairs = {
        ']' : '[',
        ')' : '(',
        '}' : '{'
    }
    for operand in rotate:
        if operand in '([{':
            stack.append(operand)
        else: 
            if stack and stack[-1] == pairs[operand]:
                stack.pop()
            else:
                return False
    if not stack:
        return True
    else:
        return False
        
def solution(s):
    cnt = 0
    for i in range(len(s)):
        rotate = s[i:] + s[:i]
        
        if is_valid(rotate):
            cnt += 1
    return cnt        