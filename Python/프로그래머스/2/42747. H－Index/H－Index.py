def solution(citations):
    #h번이상, h편이상
    citations.sort() #[0, 1, 3, 5, 6]
    for i in range(len(citations)):
        remain = len(citations) - i 
        if citations[i] >= remain:
            return remain
    return 0