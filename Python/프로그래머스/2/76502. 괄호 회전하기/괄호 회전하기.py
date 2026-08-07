def solution(s):
    def is_correct(operand):
        stack = []
        pair = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for i in operand:
            if i in '([{':
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack[-1]!=pair[i]:
                    return False
                stack.pop()
        if not stack:
            return True
        return False
            
    cnt = 0
    for i in range(len(s)):
        rotate = s[i:] + s[:i]
        if is_correct(rotate):
            cnt += 1
    return cnt
        