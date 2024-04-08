"""
def gcd(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

def solution(arr):
    answer = arr[0]
    
    for i in arr:
        answer=(answer*i)//gcd(answer,i)
    
    return answer
    
"""

import math

def solution(arr):
    answer = arr[0]
    
    for i in arr:
        answer=(answer*i)//math.gcd(answer,i)
    
    return answer