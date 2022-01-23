N,M = map(int,input().split())
S = list(input().split())
T = list(input().split())
d = dict()
for i in range(M):
    d[T[i]] = i

for x in range(N):
    if S[x] in d:
        print("Yes")
    else:
        print("No")
