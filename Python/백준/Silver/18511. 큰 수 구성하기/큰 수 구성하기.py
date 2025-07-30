def find_max_number(N, num):
    num.sort(reverse=True)
    
    max_num = 0 
    
    def recurse(current_num):
        nonlocal max_num 
        if current_num > N: 
            return 
        if current_num > max_num: 
            max_num = current_num
        for i in num: 
            recurse(current_num * 10 + i)
            
    recurse(0)
    return max_num 

# 입력 
N, K = map(int, input().split())
num = list(map(int, input().split()))

# 출력
print(find_max_number(N, num))
