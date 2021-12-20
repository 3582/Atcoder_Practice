N = int(input())
s = list(map(int, input().split()))
s.sort(reverse=True)
# a = 0
# b = 0
# for i in range(N):
#     if i %2 == 0:
#         a += s[i]
#     else:
#         b += s[i]
# print(a-b)
print(sum(s[::2]))
print(sum(s[1::2]))
# 増分stepを指定
print(sum(s[::2])-sum(s[1::2]))
