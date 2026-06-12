def solution(nums):
    set_nums = set(nums)
    type = min(len(set_nums), len(nums)//2)
    return type