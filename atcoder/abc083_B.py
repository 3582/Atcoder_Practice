import math

N, A, B = map(int, input().split())
x=0
re=0
for num in range(N):
    ans=0
    while num > 0:
        ans += num  % 10
        print(num)
        num = math.floor(num/10)
    if A<ans<B:
        re += ans
print(re)