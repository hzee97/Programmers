def solution(nums):
    answer = 0
    
    nums_set=list(set(nums))
    answer=min(len(nums)//2,len(nums_set))
    
    return answer