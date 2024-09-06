# [PCCE 기출문제] 3번_수 나누기

number = int(input())

answer = 0

for i in range(len(str(number))):
    answer += number % 100
    number //= 100

print(answer)