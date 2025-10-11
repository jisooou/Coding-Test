# A[1,2,4] B[5,4,4] : A최소값*B최대값=5+8+16=29
def solution(A,B):
    answer = 0

    A_sort = sorted(A) #A[1,2,4] 오름차순
    B_sort = sorted(B, reverse=True) #B[5,4,4] 내림차순
    
    #2개의 리스트를 같은 인덱스로 접근하기 위해=> zip()
    for a,b in zip(A_sort, B_sort): 
        answer += a * b
    
    return answer