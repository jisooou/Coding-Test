def solution(nums):
    select = len(nums) // 2
    num_set = len(set(nums))
    return min(select, num_set)