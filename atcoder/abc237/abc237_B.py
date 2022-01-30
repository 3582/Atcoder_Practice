H, W = map(int, input().split())
a = [list(map(int, input().split())) for l in range(H)]
print(a)
for w in range(W):
    for h in range(H):
        print(a[h][w], end = " ")
    print()
# d=dict()
# for i in range(W):
#     for j in range(H):
#         if not key in d:
#             d[key] = [i]
#         else:
#             d[key].append(i)