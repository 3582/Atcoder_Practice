#!/usr/bin/env PyPy3
# acc s main.py -- --guess-python-interpreter pypy
V, A, B, C = map(int, input().split())
ans = ""
while True:
    V =  V - A
    if V < 0:
        ans = "F"
        break
    V = V - B
    if V < 0:
        ans = "M"
        break
    V = V - C
    if V < 0:
        ans = "T"
        break
print(ans)