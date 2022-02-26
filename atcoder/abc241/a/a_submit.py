#!/usr/bin/env PyPy3
# acc s main.py -- --guess-python-interpreter pypy
l = list(map(int, input().split()))
ans = 0
for i in range(3):
    ans = l[ans]
print(ans)