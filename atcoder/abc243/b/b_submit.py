#!/usr/bin/env PyPy3
# acc s main.py -- --guess-python-interpreter pypy
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
d = dict()
ans_1 = 0
ans_2 = 0
for i in range(N):
    key = A[i]
    if not key in d:
        d[key] = [i]
    else:
        d[key].append(i)
        
for j in range(N):
    if B[j] in d:
        if j in d[B[j]]:
            ans_1 += 1
        else:
            ans_2 += 1
print(ans_1)
print(ans_2)