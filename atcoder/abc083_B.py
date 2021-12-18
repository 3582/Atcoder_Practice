# import math

# N, A, B = map(int, input().split())
# x=0
# re=0
# for num in range(N +1):
#     ans=0
#     numans=num
#     while num > 0:
#         ans += num % 10
#         num = math.floor(num/10)
#     if A<=ans<=B:
#         re += numans
# print(re)

a,b,c = map(int,input().split())
x = 0
for n in range(1,a+1):
    s = sum(list(map(int,list(str(n)))))
    if b <= s <= c: x += n
print(x)