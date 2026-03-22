T = int(input())
for _ in range(T):
    paran = input().strip()
    stack = []
    
    for ch in paran: 
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else: 
                stack.append(ch)
                break
            
    if stack: 
        print("NO")
    else: 
        print("YES")