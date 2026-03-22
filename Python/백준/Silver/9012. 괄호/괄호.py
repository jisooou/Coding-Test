T = int(input())
for _ in range(T):
    paran = input().strip()
    stack = []
    is_state = True
    
    for ch in paran: 
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else: 
                is_state = False
                break
            
    if stack or not is_state: 
        print("NO")
    else: 
        print("YES")