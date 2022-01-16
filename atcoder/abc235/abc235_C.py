# N, Q = map(int, input().split())
# a = list(map(int, input().split()))
# xk = [map(int, input().split()) for _ in range(Q)]
# x, k = [list(i) for i in zip(*xk)]

# for i in range(Q):
#     result = x[i] in a
#     if result:
#         count = 0
#         for j in range(len(a)):
#             if a[j] == x[i]:
#                 count += 1
#                 ans = j+1
#             if count == k[i]:
#                 print(ans)
#                 break
#         if count != k[i]:
#             print(-1)
#     else:
#         print(-1)
# 
N,Q=map(int,input().split())
# ex:[1 1 2 3 1 2]
a=list(map(int,input().split()))

d=dict()
for i in range(N):
    # リスト内の数字を取得してキーに格納（ex:1）
    key = a[i]
    # キーが辞書に存在しない場合、辞書のキーをリスト内の数字の種類にする
    # {1: }
    if not key in d:
        d[key] = [i]
    else:
        # 辞書のキー（リスト内の数字の種類）にインデックス番号(出現位置)をvalueに格納
        # {1: [0, 1, 4]}
        d[key].append(i)

for q in range(Q):
    x,k=map(int,input().split())
    # 辞書に対象の数字が存在しない場合
    if x not in d:
        print(-1)
        continue
    # 辞書内の対象の数字が出現位置より小さい場合
    if len(d[x])<k:
        print(-1)
        continue
    # 辞書内の対象の数字が出現する位置を出力
    print(d[x][k-1]+1)