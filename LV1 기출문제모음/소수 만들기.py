# Summer/Winter Coding(~2018)

from itertools import combinations

def prime(n):
	for i in range(2,int(n**0.5)+1):
		if(n%i==0):
			return False
	return True
    
def solution(nums):
    answer = 0

    case=list(combinations(nums,3))
    arr=[]
    for i in case:
        arr.append(sum(i))
    
    for i in arr:
        if prime(i)==True:
            answer+=1
    
    return answer