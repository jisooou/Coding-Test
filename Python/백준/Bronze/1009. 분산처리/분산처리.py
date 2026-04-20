# a==1 -> 1
# a==2 -> 2, 4, 8, 6
# a==3 -> 3, 9, 7, 1
# a==4 -> 4, 6
# a==5 -> 5
# a==6 -> 6
# a==7 -> 7, 9, 3, 1
# a==8 -> 8, 4, 2, 6
# a==9 -> 9, 1
# a==10 -> 0

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    a %= 10
    
    if a == 0: 
        print(10)
    elif a in [1, 5, 6]: 
        print(a)
    elif a in [4, 9]:
        if b % 2 == 1: 
            print(a)
        else:
            print((a*a)%10)
    else: 
        num = b % 4
        if num == 0: 
            num = 4
        print((a**num)%10)