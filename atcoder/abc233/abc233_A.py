import math
X, Y = map(int, input().split())
z = Y-X
ans = 0
if z > 0:
    ans = z/10
print(math.ceil(ans))