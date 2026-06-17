def solution(sizes):
    result = 0
    big_value = 0
    small_value = 0
    for x, y in sizes:
        big = max(x,y) 
        small = min(x,y) 
        big_value = max(big_value, big)
        small_value = max(small_value, small)
    return big_value*small_value