N = int(input())
A = list(map(int, input().split()))
d = dict()

for i in range(361):
    d[i] = 0

d[0] = 1
now = 0
for i in range(N):
    if now - A[i] < 0:
        now = 360 - A[i] + now
        d[now] = 1
    else:
        now = now - A[i]
        d[now] = 1

keys = [k for k, v in d.items() if v == 1]
# print(keys)
ans =[]
for i in range(len(keys)):
    if keys[i] == 0:
        ans.append(360 - keys[len(keys)-1])
    else:
        ans.append(keys[i] - keys[i-1])
print(max(ans))