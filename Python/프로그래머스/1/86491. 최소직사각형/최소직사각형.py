def solution(sizes):
    big_value, small_value = 0, 0
    for x, y in sizes:
        big = max(x, y)
        small = min(x, y)
        big_value = max(big_value, big)
        small_value = max(small_value, small)
    return big_value*small_value