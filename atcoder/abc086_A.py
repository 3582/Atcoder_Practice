# 二つの正整数 a, b が与えられます。 a と b の積が偶数か奇数か判定してください。

# 1≤a,b≤100001≤a,b≤10000
# a, b は整数

a,b = map(int, input().split())

if a * b % 2 == 0:
    print("Even")
else:
    print("Odd")