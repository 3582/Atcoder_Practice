# s = int(input()) 
# l = list(map(int, input().split()))

# # 重複を除く
# num = list(dict.fromkeys(l))

# # print(num)
# num_list = [i for i in l if i != num[0]]
# for x in range(len(num)-1):
#     num_list2 = [i for i in l if i != num[x+1]]
#     if num_list[x] > num_list2[x]:
#         num_list = num_list2
#     elif num_list[x] == num_list2[x]:
#         for y in range(len(num_list)):
#             if num_list[y] > num_list2[y]:
#                 num_list = num_list2
#                 break
# print(num_list)

#!/usr/local/bin/pypy3
import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)

n=int(readline())
a=list(map(int,readline().split()))

x=a[-1]
for i in range(n-1):
	if a[i]>a[i+1]:
		x=a[i]
		break

a=[v for v in a if v!=x]
print(*a)
