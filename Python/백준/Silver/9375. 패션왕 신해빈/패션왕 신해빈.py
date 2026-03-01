import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    clothes = {}
    n = int(input())
    for _ in range(n):
        a, b = input().strip().split()
        clothes[b]= clothes.get(b, 0) + 1 
    total = 1
    for value in clothes.values(): #카운트 한 숫자만 가져오기
        total *= (value + 1)
    print(total - 1)