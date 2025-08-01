def monkey_stack(stack_input):
	stack = []
	max_depth = 0
	
	for c in stack_input:
		if c == '[':
			stack.append('[')
			max_depth = max(max_depth, len(stack))
		elif c == ']':
			if stack: 
				stack.pop()
				
	return 2 ** max_depth if max_depth > 0 else 1 


# 입력 처리 
N = int(input())
for _ in range(N): 
	stack_input = input().strip()
	print(monkey_stack(stack_input))