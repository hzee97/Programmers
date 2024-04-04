import sys
input=sys.stdin.readline

n=int(input())

x=[]
for i in range(n):
    x.append(int(input()))

x.sort()

print(x)