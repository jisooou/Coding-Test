import sys
input = sys.stdin.readline

while True: 
    try: 
        N = int(input())
    except:
        break
    remain = 1 % N 
    ans_len = 1
    
    while remain != 0: 
        remain = (remain * 10 + 1) % N 
        ans_len += 1
    print(ans_len)