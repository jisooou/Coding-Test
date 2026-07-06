def solution(nums):
    collect = set(nums) 
    can_len = len(nums)//2
    return min(len(collect), can_len)