def solution(s):
    cnt = 0
    for i in range(len(s)):
        operand = s[i:] + s[:i]
        
        if is_valid(operand): 
            cnt += 1
    return cnt
    
def is_valid(operand):
    stack = []
    pairs = {
        ']' : '[',
        ')' : '(', 
        '}' : '{'
    }
    for o in operand:
        if o in '[({':
            stack.append(o)
        else:
            if stack and stack[-1] == pairs[o]:
                stack.pop()
            else:
                return False
    if not stack:
        return True
    else:
        return False