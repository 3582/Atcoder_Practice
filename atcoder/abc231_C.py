# N, Q = map(int, input().split())
# A = list(map(int, input().split()))
# X  = []
# Q_r = list(range(Q))
# N_r = list(range(N))
# for _ in Q_r:
#     X.append(int(input()))

# for x_num in Q_r:
#     ans = []
#     for num in N_r:
#         if(A[num] >= X[x_num]):
#             ans.append(A[num])
    
#     print(len(ans))

import bisect
N,Q=map(int,input().split())
A=list(map(int,input().split()))
# 昇順にソート
A.sort()

for i in range(Q):
    x=int(input())
    # bisect_left二部探索（前方left）により位置を把握
    # 全体の数 - 探索する対象の値の位置
    # 
    # 0,1,2,3,4,5 2以上の数は？
    # bisectにより2番目に2が入る
    # 要素数6-2=4により2以上の個数は4
    print(len(A)-bisect.bisect_left(A,x))