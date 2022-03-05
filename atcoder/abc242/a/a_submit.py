#!/usr/bin/env PyPy3
# acc s main.py -- --guess-python-interpreter pypy
A, B, C, X = map(int, input().split())
ans = 0
a = B - A
if A < X <= B:
    ans = C / a
elif X <= A:
    ans = 1
elif A < X:
    ans = 0
print(ans)