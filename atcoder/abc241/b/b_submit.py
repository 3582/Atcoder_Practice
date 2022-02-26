#!/usr/bin/env PyPy3
# acc s main.py -- --guess-python-interpreter pypy
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 'Yes'
for i in range(M):
    if B[i] in A:
        A.remove(B[i])
    else:
        ans = 'No'
print(ans)