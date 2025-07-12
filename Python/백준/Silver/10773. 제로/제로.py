# 0일 때는 pop, 0이 아닐 때는 append

import sys

def main():
    input = sys.stdin.readline
    K = int(input())
    
    stack = []
    
    for _ in range(K):
        num = int(input())
        if num == 0:
            stack.pop()
        else:
            stack.append(num)
    print(sum(stack))
    
if __name__== "__main__":
    main()