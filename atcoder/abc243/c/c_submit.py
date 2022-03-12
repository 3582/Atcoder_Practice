#!/usr/bin/env PyPy3
# acc s main.py -- --guess-python-interpreter pypy
N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
S = list(input())
