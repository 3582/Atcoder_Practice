import collections

N = int(input())
l = list(map(int, input().split()))
ans = collections.Counter(l)
print(ans.most_common()[-1][0])
