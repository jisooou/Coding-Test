import sys
input = sys.stdin.readline

A, B, C = map(int, input().split()) # 5 3 1
cnt = [0] * 101 # 문제조건

for _ in range(3):
    x, y = map(int, input().split()) # 1 6
    for i in range(x, y):
        cnt[i] += 1
 
price = 0 
for car in range(1, 101): # 문제조건 
    if cnt[car] == 1: 
        price += A 
    elif cnt[car] == 2:
        price += B*2
    elif cnt[car] == 3: 
        price += C*3
print(price)