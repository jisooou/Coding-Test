# 스택 push, pop으로 푼다.
# 처음부터 stack에 값을 다 넣는다고 생각하지 말고, 순회하면서 push/pop을 한다.

def solution(s):
    stack = []
    for ch in s: 
        if stack and stack[-1] == ch: 
            stack.pop()
        else:
            stack.append(ch)
    return 0 if stack else 1