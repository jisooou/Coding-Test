import sys

def is_good(word:str)->bool:
    stack = []
    if len(word) % 2 == 1: 
        return False 
    for ch in word: 
        if stack and stack[-1] == ch: 
            stack.pop()
        else:
            stack.append(ch)
    return not stack 


input = sys.stdin.readline
num = int(input())
cnt = 0 
for _ in range(num):
    word = input().strip()
    if is_good(word):
        cnt = cnt + 1
print (cnt)