#해시 - dict{key,value}
def solution(nums):
    #nums 리스트를 순회하는 동안에 각 숫자들이 몇번씩 나왔는지 cnt
    #예) [3,3,3,2,2,4] - 3:3번, 2:2번, 4:1번 => (3,3) (2,2) (4,1)
    #nums/2 만큼 고를 수 있다. 예) 6 // 2 = 3개 고를 수 있다. 
    #key의 개수 중에서 고를 수 있는만큼 고른다 -> key 개수: 3,2,4 => 3개 고를 수 있음 => OK. 
    
    #해시 사용한 코드--------------
    hash_nums = len(set(nums)) #중복을 제거한 종류 개수 
    my_nums = len(nums) // 2 #선택할 수 있는 개수 
    answer = min(hash_nums, my_nums)
    return answer
    
    
    #해시 사용하지 않은 코드--------------
#     cnt = 1
#     total_cnt = len(nums)
#     nums_sort = sorted(nums) #[2,2,3,3,3,4]
#     for i in range(1, total_cnt): 
#         if (nums_sort[i] != nums_sort[i-1]):
#             cnt += 1 #nums_sort 안에 있는 종류의 개수를 구함 

#     if (total_cnt//2) >= cnt: 
#         answer = cnt 
#     elif (total_cnt//2) < cnt: 
#         answer = (total_cnt//2)
#     return answer
