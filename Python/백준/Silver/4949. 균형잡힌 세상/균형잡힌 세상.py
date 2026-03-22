while True: 
    stack = []
    sentence = input()
    is_state = True
    
    if sentence == '.':
        break
    
    for ch in sentence: 
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else: 
                is_state = False
                break
        elif ch == '[':
            stack.append(ch)
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else: 
                is_state = False
                break
            
    if stack or not is_state: 
        print("no")
    else: 
        print("yes")