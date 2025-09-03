import sys 

def balance_world(line: str) -> str: 
    stack = [] 
    for ch in line:
        if ch in '([':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                return "no"
            stack.pop()
        elif ch == ']':
            if not stack or stack[-1] != '[':
                return "no"
            stack.pop()
    return "yes" if not stack else "no"

input = sys.stdin.readline
while True: 
    line = input().rstrip()
    if line == '.':
        break 
    print(balance_world(line))