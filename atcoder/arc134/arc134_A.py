# # N枚のシート、Lの橋、Wのシート
# # N L W
# # 左端からai番目にシートN枚
# # a ⋯ aN
# N,L,W = map(int, input().split())
# a = list(map(int, input().split()))

# def func(start,end,w_length):
#     return (end-start)/w_length

import math
 
N,L,W = map(int,input().split())
A = list(map(int,input().split()))
A += [L]
ans = 0
right = 0
 
for i in range(0,N + 1):
  print("a","r",A[i],right)
  if A[i] > right:
    ans += ((A[i] - right + W - 1) // W)
  right = A[i] + W
  
print(ans)
print(A)
